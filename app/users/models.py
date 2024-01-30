from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse



class Subscription(models.Model):
    class CHOICES(models.TextChoices):
      FREE = 'free', 'Бесплатная'
      BASIC = 'basic', 'Базовая'
      PREMIUM = 'premium', 'Премиум'
      VIP = 'vip', 'VIP'
      
      
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription')
    subscription_type = models.CharField(max_length=255, choices=CHOICES.choices, default=CHOICES.FREE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    max_photos = models.PositiveIntegerField()
    max_videos = models.PositiveIntegerField()
    max_audio = models.PositiveIntegerField()
    max_links = models.PositiveIntegerField()
    max_profiles = models.PositiveIntegerField()


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        
    
class MemoryPage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='memory_pages')
    deceased_first_name = models.CharField(max_length=255, blank=True, null=True)
    deceased_last_name = models.CharField(max_length=255, blank=True, null=True)
    deceased_middle_name = models.CharField(max_length=255, blank=True, null=True)
    deceased_birth_date = models.DateField(blank=True, null=True)
    deceased_death_date = models.DateField(blank=True, null=True)
    epitaph = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='photo/avatars/', blank=True, null=True)
    #Расширенная информация для платных подписок
    biography = models.TextField(null=True, blank=True)
    place_of_birth = models.CharField(max_length=255, blank=True, null=True)
    place_of_death = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    spouse = models.CharField(max_length=255, blank=True, null=True)
    profession = models.CharField(max_length=255, null=True, blank=True)

    photo_gallery = models.JSONField(null=True, blank=True)
    video_gallery = models.JSONField(null=True, blank=True)
    audio_gallery = models.JSONField(null=True, blank=True)
    guestbook = models.JSONField(null=True, blank=True) 
    significant_places = models.JSONField(null=True, blank=True) # List of places
    creative_works = models.JSONField(null=True, blank=True) # List of creative works
    awards = models.JSONField(null=True, blank=True) # List of awards
    education = models.JSONField(null=True, blank=True) # List of educational institutions
    family_composition = models.JSONField(null=True, blank=True) # List of family members
    hobbies = models.JSONField(null=True, blank=True) # List of hobbies

    def get_absolute_url(self):
        return reverse('memory-page-detail', args=[str(self.id)])

    def is_paid(self):
        return self.user.subscription.subscription_type != 'free'
    
    def __str__(self):
        return f'{self.deceased_first_name} {self.deceased_last_name} Memory Page'
# class Subscription(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     max_photos = models.PositiveIntegerField()
#     max_videos = models.PositiveIntegerField()
#     max_audio = models.PositiveIntegerField()
#     max_links = models.PositiveIntegerField()
 

#     def __str__(self):
#         return self.name

# class Permissions(models.Model):
#     subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name='permissions')
#     can_add_photos = models.BooleanField(default=False,  verbose_name='Разрешить добавлять фотографий')
#     can_add_videos = models.BooleanField(default=False, verbose_name='Разрешить добавлять видео')
#     can_add_audio = models.BooleanField(default=False, verbose_name='Разрешить добавлять аудио')
#     can_add_links = models.BooleanField(default=False, verbose_name='Разрешить добавлять ссылки')
#     can_add_reviews = models.BooleanField(default=False, verbose_name='Разрешить добавлять отзывы')
#     can_add_place_of_birth = models.BooleanField(default=False, verbose_name='Разрешить добавлять место рождения')
#     cann_add_place_of_death = models.BooleanField(default=False, verbose_name='Разрешить добавлять место смерти')
#     can_add_spouse = models.BooleanField(default=False, verbose_name='Разрешить добавлять супруга')
#     can_add_nationality = models.BooleanField(default=False, verbose_name='Разрешить добавлять национальность')
#     can_add_occupation = models.BooleanField(default=False, verbose_name='Разрешить добавлять профессию')
#     can_add_awards = models.BooleanField(default=False, verbose_name='Разрешить добавлять награды')
#     can_add_education = models.BooleanField(default=False, verbose_name='Разрешить добавлять образование')
#     can_add_family_members = models.BooleanField(default=False, verbose_name='Разрешить добавлять членов семьи')
#     can_add_hobbies_interests = models.BooleanField(default=False, verbose_name='Разрешить добавлять хобби и интересы')
#     can_add_life_milestones = models.BooleanField(default=False, verbose_name='Разрешить добавлять вехи жизни')
#     can_add_personal_anecdotes = models.BooleanField(default=False, verbose_name='Разрешить добавлять личные анекдоты')
#     can_add_significant_places = models.BooleanField(default=False, verbose_name='Разрешить добавлять значимые места')

#     class Meta:
#         verbose_name = 'Разрешение'
#         verbose_name_plural = 'Разрешения'
        
#     def __str__(self):
#         return self.subscription.name
    
    
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#     user_avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
#     subscription = models.ForeignKey(
#         Subscription, on_delete=models.SET_NULL, null=True)
    
    
#     def get_permission(self):
#         return Permissions.objects.get(subscription=self.subscription)
    
#     class Meta:
#         verbose_name = 'Профиль пользователя'
#         verbose_name_plural = 'Профили пользователей'

#     def __str__(self):
#         return f'{self.user.username} Profile'
    
    
# class MemoryPage(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='memory_pages')
#     deceased_first_name = models.CharField(max_length=255, blank=True, null=True)
#     deceased_last_name = models.CharField(max_length=255, blank=True, null=True)
#     deceased_middle_name = models.CharField(max_length=255, blank=True, null=True)
#     deceased_birth_date = models.DateField(blank=True, null=True)
#     deceased_death_date = models.DateField(blank=True, null=True)
#     epitaph = models.TextField(blank=True, null=True)
#     biography = models.TextField(blank=True, null=True)
#     page_avatar = models.ImageField(upload_to='page_avatar/', blank=True, null=True)

#     qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)


#     def get_absolute_url(self):
#         return reverse('memory-page-detail', args=[str(self.id)])
    

#     def __str__(self):
#         return f'{self.deceased_first_name} {self.deceased_last_name} Memory Page'
    
#     class Meta:
#         verbose_name = 'Страница памяти'
#         verbose_name_plural = 'Страницы памяти'



# class ExtendedMemoryPageInfo(models.Model):
#     memory_page = models.OneToOneField(
#         MemoryPage,
#         on_delete=models.CASCADE,
#         blank=True,
#         null = True,
#         verbose_name = 'Страница памяти'
#     )
#     place_of_birth = models.CharField(max_length=255, blank=True, null=True)
#     place_of_death = models.CharField(max_length=255, blank=True, null=True)
#     spouse = models.CharField(max_length=255, blank=True, null=True) #супруг
#     nationality = models.CharField(max_length=255, blank=True, null=True)
#     occupation = models.CharField(max_length=255, blank=True, null=True)
#     # Дополнительные поля
#     significant_places = models.TextField(blank=True, null=True)
#     life_milestones = models.TextField(blank=True, null=True)
#     personal_anecdotes = models.TextField(blank=True, null=True)
    
#     class Meta:
#         verbose_name = 'Расширенная информация'
#         verbose_name_plural = 'Расширенная информация'
        
#     def __str__(self):
#         return f'Расшеренная информация к странице памяти: \
#             Имя: {self.memory_page.deceased_first_name} \
#             Фамилия: {self.memory_page.deceased_last_name}. \
#             Пользователь: {self.memory_page.user.username}'
    
    
# class Award(models.Model):
#     memory_page_info = models.ForeignKey(ExtendedMemoryPageInfo, related_name='awards', on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     date = models.DateField(blank=True, null=True)

#     def __str__(self):
#         return f'{self.title} Award'
    
#     class Meta:
#         verbose_name = 'Награда'
#         verbose_name_plural = 'Награды'
    
    
# class Education(models.Model):
#     memory_page_info = models.ForeignKey(ExtendedMemoryPageInfo, related_name='educations', on_delete=models.CASCADE)
#     institution = models.CharField(max_length=255, blank=True, null=True)
#     degree = models.CharField(max_length=255, blank=True, null=True)
#     description = models.TextField()
#     years_attended = models.CharField(max_length=255, blank=True, null=True)


#     def __str__(self):
#         return f'{self.institution} Education'
    
#     class Meta:
#         verbose_name = 'Образование'
#         verbose_name_plural = 'Образование'
    
    
# class FamilyMember(models.Model):
#     class CHOICES(models.TextChoices):
#         PARENT = 'parent', 'Родители'
#         SIBLING = 'sibling', 'Сестры/Братья'
#         CHILD = 'child', 'Дети'
#     memory_page_info = models.ForeignKey(ExtendedMemoryPageInfo, related_name='family_members', on_delete=models.CASCADE, verbose_name='Страница памяти')
#     name = models.CharField(max_length=255, verbose_name='ФИО')
#     relationship = models.CharField(max_length=255, choices=CHOICES.choices)
    
#     class Meta:
#         verbose_name = 'Член семьи'
#         verbose_name_plural = 'Члены семьи'
        
    
# class HobbyInterest(models.Model):
#     memory_page_info = models.ForeignKey(ExtendedMemoryPageInfo, related_name='hobbies_interests', on_delete=models.CASCADE)
#     description = models.TextField()

#     def __str__(self):
#         return self.description
    
#     class Meta:
#         verbose_name = 'Хобби и интересы'
#         verbose_name_plural = 'Хобби и интересы'