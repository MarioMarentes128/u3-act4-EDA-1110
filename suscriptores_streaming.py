import pandas as pd
import matplotlib.pyplot as plt
## Mario Yañez NC 1110
# 1. Crear diccionario con datos de suscriptores_streaming

suscriptores_streaming = {
    'id_usuario': [801, 802, 803, 804, 805, 806],
    'nombre': ['Ana', 'Luis', 'Sofia', 'Carlos', 'Maria', 'Jorge'],
    'plan': ['Basico', 'Estandar', 'Premium', 'Basico', 'Premium', 'Estandar'],
    'fecha_inicio': ['2022-01-01', '2021-05-15', '2023-03-10', '2022-08-20', '2020-11-05', '2023-01-10'],
    'pago_mensual': [139, 199, 299, 139, 299, 199],
    'horas_vistas_mes': [15, 30, 45, 10, 50, 25],
    'dispositivos_registrados': [2, 3, 4, 1, 4, 2],
    'metodo_pago': ['Tarjeta', 'PayPal', 'Tarjeta', 'Transferencia', 'Tarjeta', 'PayPal'],
    'renovacion_automatica': [True, True, True, False, True, True],
    'estado': ['Activo', 'Activo', 'Activo', 'Cancelado', 'Activo', 'Activo']
}

print("** ANÁLISIS EXPLORATORIO DE DATOS EDA **")
print("Exploratory Data Analysis Mario Yañez NC 1110")
print("5. Crear el diccionario con 10 listas y 6 elementos")

# 2. Convertir diccionario en DataFrame
df = pd.DataFrame(suscriptores_streaming)

print("\n--- TABLA ORIGINAL DE SUSCRIPTORES ---")
print(df)

# 3. Exportar los datos a CSV
print("+-+-+ 7. Convertir el DataFrame en archivo CSV +-+-+")

df.to_csv(
    'suscriptores_streaming_1110.csv',
    index=False,
    encoding='utf-8-sig'
)

print("\nArchivo CSV creado correctamente")

# 4. Leer el archivo CSV
print("+-+-+ 8. Leer los datos desde el archivo CSV +-+-+")
print("suscriptores_streaming_1110.csv")

df = pd.read_csv('suscriptores_streaming_1110.csv')

print("\n--- DATOS LEÍDOS DESDE CSV ---")
print(df)

print("+-+-+- 9. Análisis Exploratorio de Datos (EDA) +-+-+-+")

# 5. Primeros y últimos registros
print("+-+-+- \n1. PRIMEROS REGISTROS (Head): -+-+-+")
print(df.head(3))

print("+-+-+-\n2. ÚLTIMOS REGISTROS (Tail):-+-+-+")
print(df.tail(2))

# 6. Dimensiones y estructura
print("+-+-+ 6. DIMENSIONES Y ESTRUCTURAS +-+-+")
print(df)
print("\n3. DIMENSIONES (Filas, Columnas):", df.shape)
print("\n4. NOMBRES DE COLUMNAS:\n", df.columns)
print("\n5. TIPOS DE DATOS:\n", df.dtypes)
print("\n6. INFORMACIÓN GENERAL:")
df.info()

# 7. Estadísticas y limpieza
print("+-+-+-\n7. ESTADÍSTICAS DESCRIPTIVAS:-+-+-+")
print(df.describe())
print("\n8. VALORES FALTANTES (Nulls):")
print(df.isnull().sum())
print("\n9. REGISTROS DUPLICADOS:")
print(df.duplicated().sum())
print("\n10. VALORES ÚNICOS POR COLUMNA:")
print(df.nunique())
print("Planes únicos:", df['plan'].unique())

# 8. Análisis específico
print("\n--- ANÁLISIS ESPECÍFICO DE SUSCRIPTORES ---")
print(df)
print("----------------------------------------")
print("\n11. SUSCRIPTORES POR PLAN:")
print(df['plan'].value_counts())
print("\n12. PROMEDIO DE PAGO MENSUAL: $", df['pago_mensual'].mean())
print("13. PAGO MENSUAL MÁXIMO: $", df['pago_mensual'].max())
print("14. PAGO MENSUAL MÍNIMO: $", df['pago_mensual'].min())

# 9. Ordenamiento, filtrado y agrupación
print("\n9. ORDENAMIENTO, FILTRADO Y AGRUPACIÓN")
print("\n15. SUSCRIPTORES ORDENADOS POR PAGO MENSUAL (Mayor a menor):")
print(df.sort_values(by='pago_mensual', ascending=False))
print("\n16. SUSCRIPTORES CON PAGO MENSUAL MAYOR A $150:")
filtro = df[df['pago_mensual'] > 150]
print(filtro)
print("\n17. RESUMEN POR PLAN:")
resumen = df.groupby('plan').agg(
    suscriptores=('id_usuario', 'count'),
    pago_promedio=('pago_mensual', 'mean'),
    pago_maximo=('pago_mensual', 'max'),
    horas_promedio=('horas_vistas_mes', 'mean')
)
print(resumen)

# 18. Gráfica de barras: Suscriptores por plan
print("\n18. GRÁFICA DE BARRAS: SUSCRIPTORES POR PLAN")
conteo = df['plan'].value_counts()
plt.figure(figsize=(8, 5))
plt.bar(conteo.index, conteo.values, color='skyblue')
plt.title('Suscriptores por plan de streaming Mario 1110')
plt.xlabel('Plan')
plt.ylabel('Cantidad de suscriptores')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 19. Gráfica de barras: Pago mensual por suscriptor
print("\n19. GRÁFICA DE BARRAS: PAGO MENSUAL POR SUSCRIPTOR")
plt.figure(figsize=(8, 5))
plt.bar(df['nombre'], df['pago_mensual'], color='lightgreen')
plt.title('Pago mensual por suscriptor EDA Mario 1110')
plt.xlabel('Suscriptor')
plt.ylabel('Pago mensual en pesos')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 20. Histograma: Distribución de horas vistas
print("\n20. HISTOGRAMA: DISTRIBUCIÓN DE HORAS VISTAS")
plt.figure(figsize=(8, 5))
plt.hist(df['horas_vistas_mes'], bins=5, color='orange', edgecolor='black')
plt.title('Distribución de horas vistas por suscriptor EDA Mario 1110')
plt.xlabel('Horas vistas al mes')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 21. Gráfica de dispersión: Horas vistas vs Pago mensual
print("\n21. GRÁFICA DE DISPERSIÓN: HORAS VISTAS VS PAGO MENSUAL")
plt.figure(figsize=(8, 5))
plt.scatter(df['horas_vistas_mes'], df['pago_mensual'], color='red', s=100)
plt.title('Relación entre horas vistas y pago mensual EDA Mario 1110')
plt.xlabel('Horas vistas al mes')
plt.ylabel('Pago mensual')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 22. Diagrama de caja: Distribución de pagos mensuales
print("\n22. DIAGRAMA DE CAJA: DISTRIBUCIÓN DE PAGOS MENSUALES")
plt.figure(figsize=(7, 5))
plt.boxplot(
    df['pago_mensual'],
    patch_artist=True,
    boxprops=dict(facecolor='lightblue')
)
plt.title('Distribución de pagos mensuales (Boxplot) EDA Mario 1110')
plt.ylabel('Pago mensual')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 23. Matriz de correlación
print("\n23. MATRIZ DE CORRELACIÓN")
correlacion = df.corr(numeric_only=True)
print("\n--- MATRIZ DE CORRELACIÓN ---")
print(correlacion)
plt.figure(figsize=(9, 6))
plt.imshow(correlacion, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(
    range(len(correlacion.columns)),
    correlacion.columns,
    rotation=45
)

plt.yticks(
    range(len(correlacion.columns)),
    correlacion.columns
)

plt.title('Matriz de correlación de variables numéricas EDA Mario 1110')
plt.tight_layout()
plt.show()

print("\n--- FIN DEL ANÁLISIS EDA DE SUSCRIPTORES STREAMING ---")

print("Mario Yañez NC 1110")