"""
DICCIONARIO_UTILS.PY
Librería para consultar y manipular el diccionario Quechua-Español estructurado

Autor: Sistema de extracción automática
Fecha: 2024
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
        """
        Inicializa la librería cargando los archivos JSON
        
        Args:
            ruta_qe: Ruta al archivo JSON Quechua-Español
            ruta_eq: Ruta al archivo JSON Español-Quechua
        """
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
                if categoria:
                    self.indice_categoria[categoria].append(entrada)
                
                campo = entrada.get('campo_semantico', '')
                if campo:
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
        
        for entrada in entradas:
            dialectales = entrada.get('variantes_dialectales', {})
            for region, variante in dialectales.items():
                if variante not in variantes:
                    variantes.append(f"{region}: {variante}")
        
        return variantes
    
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
    
    def buscar_texto_completo(self, texto: str) -> List[Dict]:
        """
        Busca texto en definiciones y sinónimos
        
        Args:
            texto: Texto a buscar
            
        Returns:
            Lista de entradas que contienen el texto
        """
        texto_lower = texto.lower()
        resultados = []
        
        for entrada in self.datos_qe + self.datos_eq:
            # Buscar en definición
            definicion = entrada.get('definicion', '').lower()
            if texto_lower in definicion:
                resultados.append(entrada)
                continue
            
            # Buscar en sinónimos
            sinonimos = entrada.get('sinonimos', [])
            for sinonimo in sinonimos:
                if texto_lower in sinonimo.lower():
                    resultados.append(entrada)
                    break
        
        return resultados
    
    def estadisticas(self) -> Dict:
        """
        Genera estadísticas del diccionario
        
        Returns:
            Diccionario con estadísticas
        """
        total_entradas = self.contar_entradas()
        categorias = self.listar_categorias_gramaticales()
        campos = self.listar_campos_semanticos()
        
        # Contar variantes dialectales
        total_variantes = 0
        for entrada in self.datos_qe + self.datos_eq:
            total_variantes += len(entrada.get('variantes_dialectales', {}))
        
        # Contar sinónimos
        total_sinonimos = 0
        for entrada in self.datos_qe + self.datos_eq:
            total_sinonimos += len(entrada.get('sinonimos', []))
        
        return {
            'entradas': total_entradas,
            'categorias_gramaticales': len(categorias),
            'campos_semanticos': len(campos),
            'variantes_dialectales': total_variantes,
            'sinonimos': total_sinonimos,
            'lista_categorias': categorias,
            'lista_campos': campos
        }

# Funciones de conveniencia para uso directo
def cargar_diccionario(ruta_qe: str = "quechua_espanol.json", 
                      ruta_eq: str = "espanol_quechua.json") -> DiccionarioQuechua:
    """
    Carga el diccionario con las rutas especificadas
    
    Args:
        ruta_qe: Ruta al archivo JSON Quechua-Español
        ruta_eq: Ruta al archivo JSON Español-Quechua
        
    Returns:
        Instancia de DiccionarioQuechua
    """
    return DiccionarioQuechua(ruta_qe, ruta_eq)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancia del diccionario
    diccionario = cargar_diccionario()
    
    # Mostrar estadísticas
    stats = diccionario.estadisticas()
    print("=== ESTADÍSTICAS DEL DICCIONARIO ===")
    for clave, valor in stats.items():
        if isinstance(valor, list) and len(valor) > 10:
            print(f"{clave}: {len(valor)} elementos")
        else:
            print(f"{clave}: {valor}")
    
    # Ejemplos de búsqueda
    print("\n=== EJEMPLOS DE BÚSQUEDA ===")
    
    # Buscar por quechua
    resultados = diccionario.buscar_por_quechua("achupalla")
    if resultados:
        print(f"\nBúsqueda 'achupalla': {len(resultados)} resultado(s)")
        print(f"Definición: {resultados[0].get('definicion', 'N/A')}")
    
    # Buscar por categoría gramatical
    sustantivos = diccionario.buscar_por_categoria_gramatical("s.")
    print(f"\nSustantivos encontrados: {len(sustantivos)}")
    
    # Buscar por campo semántico
    botanicos = diccionario.buscar_por_campo_semantico("Bot.")
    print(f"Términos botánicos: {len(botanicos)}")