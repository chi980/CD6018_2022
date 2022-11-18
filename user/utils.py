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
    upload_to = f'media/{instance}'
    ext = filename.split('.')[-1]
    uuid = uuid4().hex
    if instance:
        filename = '{}_{}.{}'.format(uuid, instance, ext)
    else:
        filename = '{}.{}'.format(uuid, ext)
    return os.path.join(upload_to,filename)