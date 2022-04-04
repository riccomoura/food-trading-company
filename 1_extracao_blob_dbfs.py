# Databricks notebook source
# MAGIC %md
# MAGIC ## Mount do Blob Storage a partir de uma raw_table e armazenando no DBFS

# COMMAND ----------

# Lançamento de credenciais
_conf_key = "fs.azure.account.key.user.blob.core.windows.net"
_key = "{key}"
_chave = {_conf_key:_key}
_url_blob = "wasbs://fake-company@user.blob.core.windows.net"
path = "/mnt/henrique_mesquita"

# Prevenindo erros de execução futuros
dbutils.fs.unmount(path)

# Montando repositório do blob dentro do DBFS
dbutils.fs.mount(
    source = _url_blob,
    mount_point = path,
    extra_configs = _chave)
