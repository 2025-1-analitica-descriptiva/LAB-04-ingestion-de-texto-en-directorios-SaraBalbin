# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```
    """
    import pandas as pd
    import zipfile
    import os

    def crear_dataframe(ruta_base):
        datos = []
        for carpeta_actual, subcarpetas, archivos in os.walk(ruta_base):
            # print(f" Carpeta: {carpeta_actual}")
            # print(f" Subcarpeta: {subcarpetas}")
            # print(f" Archivo: {archivos}")
            nombre_carp_actual = os.path.basename(carpeta_actual)
            for archivo in archivos:
                ruta_archivo = os.path.join(carpeta_actual, archivo)

                with open(ruta_archivo, 'r', encoding='utf-8') as f:
                        primera_linea = f.readline().strip()
                        datos.append({
                            'phrase': primera_linea,
                            'target': nombre_carp_actual
                        })
        df = pd.DataFrame(datos)
        return df
    
    def guardar_datos(output_ruta, df, nombre):
        if not os.path.exists(output_ruta):
            os.makedirs(output_ruta)
        df.to_csv(f'{output_ruta}/{nombre}.csv', encoding='utf-8')
         
        
    zip_ruta = 'files/input.zip'
    input_ruta = 'files/input'
    output_ruta = 'files/output'

    if not os.path.exists(input_ruta):
        with zipfile.ZipFile(zip_ruta, 'r') as zip_ref:
            zip_ref.extractall('files')

    df_test = crear_dataframe(f'{input_ruta}/test')
    df_train = crear_dataframe(f'{input_ruta}/train')

    guardar_datos(output_ruta, df_test, "test_dataset")
    guardar_datos(output_ruta, df_train, "train_dataset")
