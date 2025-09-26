"""
DICCIONARIO_UTILS.PY
Librería para consultar y manipular el diccionario Quechua-Español estructurado

Autor: Ciro Gabriel Callapiña Castilla
Fecha: 2025
"""

import json
import os
from typing import List, Dict, Optional
from collections import defaultdict

class DiccionarioQuechua:
    """
    Clase principal para gestionar el diccionario Quechua-Español
    """
    
    def __init__(self, ruta_qe: str = "quechua_espanol.json", 
                 ruta_eq: str = "espanol_quechua.json"):
        self.datos_qe = self._cargar_json(ruta_qe)
        self.datos_eq = self._cargar_json(ruta_eq)
        
        # Crear índices para búsquedas rápidas
        self._crear_indices()
    
    def _cargar_json(self, ruta: str) -> List[Dict]:
        """
        Carga un archivo JSON de entradas del diccionario
        
        Args:
            ruta: Ruta al archivo JSON
            
        Returns:
            Lista de entradas del diccionario
        """
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Archivo no encontrado: {ruta}")
            return []
        except json.JSONDecodeError:
            print(f"Error decodificando JSON: {ruta}")
            return []
    
    def _crear_indices(self):
        """
        Crea índices para búsquedas eficientes
        """
        self.indice_qe = {} 
        self.indice_eq = {}
        self.indice_categoria = defaultdict(list)
        self.indice_campo = defaultdict(list)
        
        # Índice Quechua-Español
        for entrada in self.datos_qe:
            lema = entrada.get('lema', '').lower()
            if lema:
                if lema not in self.indice_qe:
                    self.indice_qe[lema] = []
                self.indice_qe[lema].append(entrada)

                # Índices por categoría y campo
                categoria = entrada.get('categoria_gramatical', '')
                if isinstance(categoria, list):
                    for cat in categoria:
                        if cat:
                            self.indice_categoria[cat].append(entrada)
                elif categoria:
                    self.indice_categoria[categoria].append(entrada)

                campo = entrada.get('campo_semantico', '')
                if isinstance(campo, list):
                    for c in campo:
                        if c:
                            self.indice_campo[c].append(entrada)
                elif campo:
                    self.indice_campo[campo].append(entrada)

        # Índice Español-Quechua
        for entrada in self.datos_eq:
            lema = entrada.get('lema', '').lower()
            if lema:
                if lema not in self.indice_eq:
                    self.indice_eq[lema] = []
                self.indice_eq[lema].append(entrada)
    
    def buscar_por_quechua(self, lema: str) -> List[Dict]:
        """
        Busca entradas por lema en quechua
        
        Args:
            lema: Palabra en quechua a buscar
            
        Returns:
            Lista de entradas que coinciden
        """
        lema_lower = lema.lower()
        return self.indice_qe.get(lema_lower, [])
    
    def buscar_por_espanol(self, lema: str) -> List[Dict]:
        """
        Busca entradas por lema en español
        
        Args:
            lema: Palabra en español a buscar
            
        Returns:
            Lista de entradas que coinciden
        """
        lema_lower = lema.lower()
        return self.indice_eq.get(lema_lower, [])
    
    def obtener_variantes_dialectales(self, lema: str) -> List[str]:
        """
        Obtiene las variantes dialectales de una palabra

        Args:
            lema: Palabra a buscar

        Returns:
            Lista de variantes dialectales 
        """
        variantes = []
        entradas = self.buscar_por_quechua(lema) + self.buscar_por_espanol(lema)

        def extraer_variantes(dialectales, pais=None):
            if isinstance(dialectales, dict):
                for region, variante in dialectales.items():
                    if isinstance(variante, dict):
                        extraer_variantes(variante, pais=region if pais is None else f"{pais}/{region}")
                    elif isinstance(variante, list):
                        clave = f"{pais}/{region}" if pais else region

                        variantes.append(f"{clave}: {', '.join(str(v) for v in variante)}")
                    else:
                        clave = f"{pais}/{region}" if pais else region
                        variantes.append(f"{clave}: {variante}")
            elif isinstance(dialectales, list):
                clave = pais if pais else ""
                variantes.append(f"{clave}: {', '.join(str(v) for v in dialectales)}")
            elif isinstance(dialectales, str):
                clave = pais if pais else ""
                variantes.append(f"{clave}: {dialectales}")

        for entrada in entradas:
            dialectales = entrada.get('variantes_dialectales', {})
            extraer_variantes(dialectales)

        # Eliminar duplicados manteniendo el orden
        variantes_unicas = []
        seen = set()
        for v in variantes:
            if v not in seen:
                variantes_unicas.append(v)
                seen.add(v)

        return variantes_unicas

    def buscar_por_categoria_gramatical(self, categoria: str) -> List[Dict]:
        """
        Busca entradas por categoría gramatical
        
        Args:
            categoria: Categoría gramatical (ej. 's.', 'adj.', 'v.')
            
        Returns:
            Lista de entradas que coinciden
        """
        return self.indice_categoria.get(categoria, [])
    
    def buscar_por_campo_semantico(self, campo: str) -> List[Dict]:
        """
        Busca entradas por campo semántico
        
        Args:
            campo: Campo semántico (ej. 'Bot.', 'Zool.', 'Med.Folk.')
            
        Returns:
            Lista de entradas que coinciden
        """
        return self.indice_campo.get(campo, [])
    
    def contar_entradas(self) -> Dict:
        """
        Cuenta el número de entradas por sección
        
        Returns:
            Diccionario con conteos por sección
        """
        return {
            'quechua_espanol': len(self.datos_qe),
            'espanol_quechua': len(self.datos_eq),
            'total': len(self.datos_qe) + len(self.datos_eq)
        }
    
    def listar_lemas(self) -> Dict:
        """
        Lista todos los lemas por sección
        
        Returns:
            Diccionario con listas de lemas por sección
        """
        return {
            'quechua_espanol': list(self.indice_qe.keys()),
            'espanol_quechua': list(self.indice_eq.keys())
        }
    
    def listar_categorias_gramaticales(self) -> List[str]:
        """
        Lista todas las categorías gramaticales disponibles
        
        Returns:
            Lista de categorías gramaticales
        """
        return list(self.indice_categoria.keys())
    
    def listar_campos_semanticos(self) -> List[str]:
        """
        Lista todos los campos semánticos disponibles
        
        Returns:
            Lista de campos semánticos
        """
        return list(self.indice_campo.keys())
    
    