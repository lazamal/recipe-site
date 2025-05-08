from django.test import TestCase
from japan_foods.models import Food
import random
from django.urls import reverse
from django.contrib.auth.models import User



# Create your tests here.




class FoodTestCase(TestCase):
    def setUp(self):
        for i in range(20):
            Food.objects.create(food_name=f'{str(random.randint(100,200)*i)}', ingredients=f'{str(random.randint(1,2)*i)}',recepie = f'{str(random.randint(1,2)*i)}',rating =(i % 5 ) +1)
        Food.objects.create(food_name=f'snail', ingredients=f'snail, lettuce',recepie = f'cook it!',rating ='5' )


    def test_food(self):
        # check if snail is on the recipe book
        snail = Food.objects.get(food_name=f'snail', ingredients=f'snail, lettuce',recepie = f'cook it!',rating ='5' )
        self.assertIn("snail",snail.food_name )

    def test_form_redirect(self):

        User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

        url = reverse('japan_foods:add_post')
        response = self.client.post(url, data={
        'food_name': 'Sushi',
        'ingredients': 'Rice, Fish',
        'recepie': 'Roll and serve.',
        'rating': 5
    })
        
        expected_url = reverse('japan_foods:index')
        self.assertRedirects(response, expected_url)
        