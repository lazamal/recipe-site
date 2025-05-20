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




        


# test_use_correct_template 
# blog/edit_post.html
# Arrange - make sure we have an existing post
# Act - get edit_post view
# Assert - check template used in respones


#  def test_index_page_uses_correct_template(self):
#         # Arrange
#         User = get_user_model()
#         user = User.objects.create_user("user", password="1234")

#         self.client.login(username=user.username, password="1234")


#         # Act
#         response = self.client.get(reverse('blog:index'))

#         # Assert
#         self.assertTemplateUsed(response, "blog/index.html")

    def test_edit_post(self):
        # Arrange
        User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        

        # act
        post_id = Food.object.id
        print(post_id)
        response = self.client.get(reverse(f'japan_foods:edit', args=[post_id]))

        # assert
        self.assertTemplateUsed(response, "japan_foods/edit_post.html")
        


# test_edit_post_call_actually_edits_post
# Arrange - make sure we have an existing post
# Act - send data to view/endpoint
