# DATABASES = {
#     'default':{
#         'ENGINE':'django.db.backends.mysql',
#         'NAME':'petzone',
#         'USER':'admin',
#         'PASSWORD':'zoqtmxhs1B!',
#         'HOST':'petzone.czjbs2fg6nlg.ap-northeast-2.rds.amazonaws.com',
#         'PORT':3306,
#         'OPTIONS':{
#             'init_command':'SET sql_mode="STRICT_TRANS_TABLES"'
#         }
#     }
# }

# S3 = {
#     'aws_access_key_id':'AKIAVTRQYLJC5KZO7PF4',
#     'aws_secret_access_key':'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',
#     'aws_storage_bucket_name':'petzonebucket',
#     'aws_querystring_auth':False
# }

DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME':'petzone',
        'USER':'root',
        'PASSWORD':'0216',
        'HOST':'localhost',
        'PORT':'3306'
    }
}


#'django-insecure-)sqstsc!nza^o)+q)z_p+0$13v$nb^8p5re5x$5#y1gok0my22'
SECRET_KEY = 'django-insecure-)q^w$$y6tenvgv=ja4v*ecvjk&!7w+tbba5tmi%@evgbelspao*'
