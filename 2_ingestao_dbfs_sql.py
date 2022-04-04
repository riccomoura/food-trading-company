# Databricks notebook source
# MAGIC %md
# MAGIC ### Criando um Data Frame a partir do arquivo montado do Blob Storage no File System do Databricks

# COMMAND ----------

# Instanciando o dataset dentro do DBFS com os parâmetros básicos
format_file = "csv"
path = "dbfs:/mnt/henrique_mesquita/orders.csv"
options = {
    "header":True,
    "delimiter":";"
}

df = spark.read \
    .format(format_file) \
    .options(**options) \
    .load(path)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Usando credenciais e chave de acesso para carregamento dos dados do DBFS para o SQL Server

# COMMAND ----------

table_name = "STAGE_henrique_mesquita.orders"
jdbcServer = "sql-user.database.windows.net"
jdbcDatabase = "db-user"
jdbcPort = 1433
jdbcUsername = "{username}"
jdbcPassword = "{password}"
jdbcUrl = f"jdbc:sqlserver://{jdbcServer}:{jdbcPort};database={jdbcDatabase};user={jdbcUsername};password={jdbcPassword}"

df.write \
    .format('jdbc') \
    .mode('overwrite') \
    .option('url', jdbcUrl) \
    .option('dbtable', table_name) \
    .save()
