def upload_image(instance,filename):
    import os
    from random import randint
    from django.utils.timezone import now
    filename_base,filename_ext = os.path.splitext(filename)

    # 파일 이름: 업로드날짜_랜덤숫자
    return '%s' % (
        now().strftime('%Y%m%d')+'_'+str(randint(10000000,99999999))
    )