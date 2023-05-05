from unittest import TestCase
from app import app
from models import User, db

app.config["DEBUG_TB_HOSTS"] = ['dont-show-debug-toolbar']

class FlaskTests(TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def create_cleanup(self):
        User.query.filter(User.first_name =='tes1', 
                            User.last_name=='ldac', 
                            User.image_url=='https://storage.googleapis.com/proudcity/mebanenc/uploads/2021/03/placeholder-image.png').delete()        
        db.session.commit()

    # test to make sure a bullet point is made for every user
    def test_user_list(self):
        with self.client as client:
            res = client.get('users')
            html = res.get_data(as_text=True)
            user_list = User.query.all()
            for user in user_list:
                self.assertIn(f'{user.first_name} {user.last_name}', html)
            print(user_list)

    # test to make sure /users/new creates a new user in the database
    def test_create(self):
        with self.client as client:
            user_data = {
               'first-name': 'tes1',
               'last-name': 'ldac',
               'image-url': 'https://storage.googleapis.com/proudcity/mebanenc/uploads/2021/03/placeholder-image.png'
            }
            res1 = client.post('users/new', data=user_data)
            added_user = User.query.filter(User.first_name =='tes1', 
                                           User.last_name=='ldac', 
                                           User.image_url=='https://storage.googleapis.com/proudcity/mebanenc/uploads/2021/03/placeholder-image.png').all()[0]             
            self.assertIsNotNone(added_user)           
            self.create_cleanup()
            
            
    # test to make sure /users/delete deletes new user in the database
    def test_delete(self):
        remove_target = User(first_name="removeme101", last_name="removeme101", image_url="removeme101")
        db.session.add(remove_target)
        db.session.commit()
    
        with self.client as client:
            to_be_removed_id = remove_target.id
            self.assertEqual(len(User.query.filter(User.first_name=="removeme101").all()), 1)
            res = client.post(f'users/{to_be_removed_id}/delete')
            self.assertEqual(User.query.filter(User.first_name=="removeme101").all(), [])

    # test to make sure /users/edit edits a user in the database
    def test_edit(self):
        edit_target = User(first_name="editme101", last_name="editme101", image_url="editme101")
        new_user_data = {
               'first-name': 'tes1',
               'last-name': 'ldac',
               'image-url': 'https://storage.googleapis.com/proudcity/mebanenc/uploads/2021/03/placeholder-image.png'
            }
        
        db.session.add(edit_target)
        db.session.commit()
        
        with self.client as client:
            edit_target_id = edit_target.id
            res = client.post(f'users/{edit_target_id}/edit', data=new_user_data)
            user = User.query.filter(User.id==edit_target_id).all()[0]
            self.assertEqual(new_user_data['first-name'], user.first_name)
            self.assertEqual(new_user_data['last-name'], user.last_name)
            self.assertEqual(new_user_data['image-url'], user.image_url)
            client.post(f'users/{edit_target_id}/delete')
            
            