# Databricks notebook source
# MAGIC %md
# MAGIC ## Mount do Blob Storage a partir de uma raw_table e armazenando no DBFS

# COMMAND ----------

# Lançamento de credenciais
_conf_key = "fs.azure.account.key.stgestudos.blob.core.windows.net"
_key = "j+Ji7MO3YLhkwCarp8OCzbgy2ENitNs09cF8Sm2q2IU1UZGo82VKSmuVXidZeUEn4/ljKtItIB1ZW6JVd1YAuQ=="
_chave = {_conf_key:_key}
_url_blob = "wasbs://pocco-company@stgestudos.blob.core.windows.net"
path = "/mnt/henrique_mesquita"

# Prevenindo erros de execução futuros
dbutils.fs.unmount(path)

# Montando repositório do blob dentro do DBFS
dbutils.fs.mount(
    source = _url_blob,
    mount_point = path,
    extra_configs = _chave)