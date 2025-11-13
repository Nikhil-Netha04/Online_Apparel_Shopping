import pymysql
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
pymysql.version_info = (1, 4, 2, "final", 0)
pymysql.install_as_MySQLdb()