### DB設定
```
pip install dj-database-url
pip install python-dotenv
pip install mysqlclient
```

### 設定ファイル
##### blogs/settings.py
```
import dj_database_url
from dotenv import (
    find_dotenv,
    load_dotenv,
)
load_dotenv(find_dotenv())
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600),
}
```

### MySQLプロジェクトDB作成
```
mysql -u root
> ALTER USER 'root'@'localhost' IDENTIFIED BY 'password';
> create database <DB名>;
```
##### これ以降：
```
> ALTER USER 'root'@'localhost' IDENTIFIED BY 'password';
```
##### MySQLログイン(パスワード指定)：
```
mysql -u root -p
> Enter password
```

#### 環境設定ファイル(.env)
```
DATABASE_URL=mysql://root:password@localhost/<DB名>
```

#### 接続確認
```
python manage.py migrate
```

#### スーパーユーザー（管理者）作成
```
$ python manage.py createsuperuser

> ユーザー名 (leave blank to use 'user'): 
> メールアドレス: 
> Password: 
> Password (again): 
このパスワードは一般的すぎます。
Bypass password validation and create user anyway? [y/N]: y
```

参考:https://github.com/shun-rec/django-website-05