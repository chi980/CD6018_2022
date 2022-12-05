def upload_image(instance,filename):
    import os
    from random import randint
    from django.utils.timezone import now
    filename_base,filename_ext = os.path.splitext(filename)

    # 파일 이름: 업로드날짜_랜덤숫자
    return '%s' % (
        now().strftime('%Y%m%d')+'_'+str(randint(10000000,99999999))
    )

def rename_image(instance,filename):
    import os
    from uuid import uuid4
    # print("&&&&&&&&&&&&&&&&&&&&&&&&&utils.py")
    # print(type(instance))
    # print(instance.user)
    upload_to = f'media/pet/{instance.user.id}/'
    ext = filename.split('.')[-1]
    uuid = uuid4().hex
    if instance:
        filename = '{}_{}.{}'.format(uuid, instance, ext)
    else:
        filename = '{}.{}'.format(uuid, ext)
    return os.path.join(upload_to,filename)

def rename_category_image(instance, filename):
    import os
    from uuid import uuid4
    print(filename)
    upload_to = f'media/'
    ext = filename.split('.')[-1]
    uuid = uuid4().hex
    filename = '{}.{}'.format(uuid, ext)
    return os.path.join(upload_to,filename)
