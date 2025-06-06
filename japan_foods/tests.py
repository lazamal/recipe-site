from django.test import TestCase
from japan_foods.models import Food, Comment
import random
from django.urls import reverse
from django.contrib.auth.models import User



# Create your tests here.


class FoodTestCase(TestCase):
    

    def setUp(self):
        for i in range(20):
            Food.objects.create(food_name=f'{str(random.randint(100,200)*i)}', ingredients=f'{str(random.randint(1,2)*i)}',recepie = f'{str(random.randint(1,2)*i)}',rating =(i % 5 ) +1)
        Food.objects.create(food_name=f'snail', ingredients=f'snail, lettuce',recepie = f'cook it!',rating ='5' )

        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

        self.food = Food.objects.get(food_name='snail')
        self.food2 = Food.objects.exclude(id=self.food.id).first()

    def test_food(self):
        # check if snail is on the recipe book
        snail = Food.objects.get(food_name=f'snail', ingredients=f'snail, lettuce',recepie = f'cook it!',rating ='5' )
        self.assertIn("snail",snail.food_name )

    def test_form_redirect(self):
        # check that create food form properly works

        url = reverse('japan_foods:add_post')
        response = self.client.post(url, data={
        'food_name': 'Sushi',
        'ingredients': 'Rice, Fish',
        'recepie': 'Roll and serve.',
        'rating': 5
    })
        
        expected_url = reverse('japan_foods:index')
        self.assertRedirects(response, expected_url)


    def test_access_edit_post(self):
        # checking is a user can access the edit page

        # Arrange
        
        
        

        # act
        response = self.client.get(reverse(f'japan_foods:edit_post', args=[self.food.id]))

        # assert
        self.assertTemplateUsed(response, "japan_foods/edit_post.html")

class CommentTestCase(FoodTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('japan_foods:index')
        self.response = self.client.post(self.url, data={
        'form_type': 'comment_form',
        'food_id': self.food.id,
        'text': 'my comment',
        'writer': 'Ali baba'
    })
        self.comment = Comment.objects.filter(food=self.food, text='my comment').first()




    # test adding a comment
    def test_add_comment(self):

        # assert redirect
        expected_url = reverse('japan_foods:index')
        self.assertRedirects(self.response, expected_url)

        # assert comment was created
       
        self.assertIsNotNone(self.comment)
        self.assertEqual(self.comment.writer, 'Ali baba')
        self.assertEqual(self.comment.food, self.food)

        # assert it belongs to food 1
        self.assertEqual(self.comment.food, self.food)

        # assert that it doesnt belong to food 2
        comments_for_food2 = Comment.objects.filter(food=self.food2)
        self.assertEqual(comments_for_food2.count(), 0)

    def test_edit_comment(self):
        # assert redirect

        expected_url = reverse('japan_foods:index')
        self.assertRedirects(self.response, expected_url)

        # assert post on edit comment form
        edit_response = self.response = self.client.post(self.url, data={
        'form_type': 'comment_edit_form',
        'comment_id': self.comment.id,
        'text': 'my edited comment'
    })
        
        self.assertRedirects(edit_response, expected_url)

        self.comment.refresh_from_db()

        self.assertEqual(self.comment.text, 'my edited comment')

     
    def test_delete_comment(self):
    # Make sure the comment exists before delete
        comment_id = self.comment.id
        self.assertTrue(Comment.objects.filter(id=comment_id).exists())

    # Send POST request to delete the comment
        delete_response = self.client.post(self.url, data={
        'form_type': 'delete_comment_form',
        'comment_id': comment_id,
    })

    # Check it redirects properly after deletion
        expected_url = reverse('japan_foods:index')
        self.assertRedirects(delete_response, expected_url)

    # Assert the comment no longer exists
        self.assertFalse(Comment.objects.filter(id=comment_id).exists())








# test_edit_post_call_actually_edits_post
# Arrange - make sure we have an existing post
# Act - send data to view/endpoint
