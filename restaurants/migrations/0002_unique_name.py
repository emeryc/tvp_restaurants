
from south.db import db
from django.db import models
from restaurants.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Changing field 'Restaurant.website'
        # (to signature: django.db.models.fields.URLField(max_length=200, blank=True))
        db.alter_column('restaurants_restaurant', 'website', orm['restaurants.restaurant:website'])
        
        # Changing field 'Restaurant.last_mod'
        # (to signature: django.db.models.fields.DateTimeField(auto_now=True, blank=True))
        db.alter_column('restaurants_restaurant', 'last_mod', orm['restaurants.restaurant:last_mod'])
        
        # Changing field 'Restaurant.address1'
        # (to signature: django.db.models.fields.CharField(max_length=50))
        db.alter_column('restaurants_restaurant', 'address1', orm['restaurants.restaurant:address1'])
        
        # Changing field 'Restaurant.address2'
        # (to signature: django.db.models.fields.CharField(max_length=50, blank=True))
        db.alter_column('restaurants_restaurant', 'address2', orm['restaurants.restaurant:address2'])
        
        # Changing field 'Restaurant.phone'
        # (to signature: django.contrib.localflavor.us.models.PhoneNumberField(blank=True))
        db.alter_column('restaurants_restaurant', 'phone', orm['restaurants.restaurant:phone'])
        
        # Changing field 'Restaurant.user'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['auth.User']))
        db.alter_column('restaurants_restaurant', 'user_id', orm['restaurants.restaurant:user'])
        
        # Changing field 'Restaurant.slug'
        # (to signature: django.db.models.fields.SlugField(max_length=50, unique=True, db_index=True))
        db.alter_column('restaurants_restaurant', 'slug', orm['restaurants.restaurant:slug'])
        
        # Changing field 'MenuItem.restaurant'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['restaurants.Restaurant']))
        db.alter_column('restaurants_menuitem', 'restaurant_id', orm['restaurants.menuitem:restaurant'])
        
        # Changing field 'MenuItem.bad_info'
        # (to signature: django.db.models.fields.BooleanField(default=False, blank=True))
        db.alter_column('restaurants_menuitem', 'bad_info', orm['restaurants.menuitem:bad_info'])
        
        # Changing field 'MenuItem.last_mod'
        # (to signature: django.db.models.fields.DateTimeField(default=datetime.datetime(2009, 7, 28, 2, 13, 54, 11930), auto_now=True, blank=True))
        db.alter_column('restaurants_menuitem', 'last_mod', orm['restaurants.menuitem:last_mod'])
        
        # Changing field 'MenuItem.is_available'
        # (to signature: django.db.models.fields.BooleanField(default=True, blank=True))
        db.alter_column('restaurants_menuitem', 'is_available', orm['restaurants.menuitem:is_available'])
        
        # Changing field 'MenuItem.user'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['auth.User']))
        db.alter_column('restaurants_menuitem', 'user_id', orm['restaurants.menuitem:user'])
        
        # Changing field 'ReferingSite.url'
        # (to signature: django.db.models.fields.URLField(max_length=200, unique=True))
        db.alter_column('restaurants_referingsite', 'url', orm['restaurants.referingsite:url'])
        
        # Changing field 'ReferingSite.restaurant'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['restaurants.Restaurant']))
        db.alter_column('restaurants_referingsite', 'restaurant_id', orm['restaurants.referingsite:restaurant'])
        
        # Changing field 'Hours.restaurant'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['restaurants.Restaurant']))
        db.alter_column('restaurants_hours', 'restaurant_id', orm['restaurants.hours:restaurant'])
        
        # Changing field 'Rating.restaurant'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['restaurants.Restaurant']))
        db.alter_column('restaurants_rating', 'restaurant_id', orm['restaurants.rating:restaurant'])
        
        # Changing field 'Rating.user'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['auth.User']))
        db.alter_column('restaurants_rating', 'user_id', orm['restaurants.rating:user'])
        
        # Creating unique_together for [name] on Restaurant.
        db.create_unique('restaurants_restaurant', ['name'])
        
    
    
    def backwards(self, orm):
        
        # Changing field 'Restaurant.website'
        # (to signature: models.URLField(blank=True))
        db.alter_column('restaurants_restaurant', 'website', orm['restaurants.restaurant:website'])
        
        # Changing field 'Restaurant.last_mod'
        # (to signature: models.DateTimeField(auto_now=True))
        db.alter_column('restaurants_restaurant', 'last_mod', orm['restaurants.restaurant:last_mod'])
        
        # Changing field 'Restaurant.address1'
        # (to signature: models.CharField("Address Line 1", max_length=50))
        db.alter_column('restaurants_restaurant', 'address1', orm['restaurants.restaurant:address1'])
        
        # Changing field 'Restaurant.address2'
        # (to signature: models.CharField("Address Line 2", max_length=50, blank=True))
        db.alter_column('restaurants_restaurant', 'address2', orm['restaurants.restaurant:address2'])
        
        # Changing field 'Restaurant.phone'
        # (to signature: PhoneNumberField(blank=True))
        db.alter_column('restaurants_restaurant', 'phone', orm['restaurants.restaurant:phone'])
        
        # Changing field 'Restaurant.user'
        # (to signature: models.ForeignKey(orm['auth.User']))
        db.alter_column('restaurants_restaurant', 'user_id', orm['restaurants.restaurant:user'])
        
        # Changing field 'Restaurant.slug'
        # (to signature: models.SlugField(unique=True))
        db.alter_column('restaurants_restaurant', 'slug', orm['restaurants.restaurant:slug'])
        
        # Changing field 'MenuItem.restaurant'
        # (to signature: models.ForeignKey(orm['restaurants.Restaurant']))
        db.alter_column('restaurants_menuitem', 'restaurant_id', orm['restaurants.menuitem:restaurant'])
        
        # Changing field 'MenuItem.bad_info'
        # (to signature: models.BooleanField(default=False))
        db.alter_column('restaurants_menuitem', 'bad_info', orm['restaurants.menuitem:bad_info'])
        
        # Changing field 'MenuItem.last_mod'
        # (to signature: models.DateTimeField(default=datetime.datetime(2009, 6, 6, 15, 30, 33, 513054), auto_now=True))
        db.alter_column('restaurants_menuitem', 'last_mod', orm['restaurants.menuitem:last_mod'])
        
        # Changing field 'MenuItem.is_available'
        # (to signature: models.BooleanField(default=True))
        db.alter_column('restaurants_menuitem', 'is_available', orm['restaurants.menuitem:is_available'])
        
        # Changing field 'MenuItem.user'
        # (to signature: models.ForeignKey(orm['auth.User']))
        db.alter_column('restaurants_menuitem', 'user_id', orm['restaurants.menuitem:user'])
        
        # Changing field 'ReferingSite.url'
        # (to signature: models.URLField(unique=True))
        db.alter_column('restaurants_referingsite', 'url', orm['restaurants.referingsite:url'])
        
        # Changing field 'ReferingSite.restaurant'
        # (to signature: models.ForeignKey(orm['restaurants.Restaurant']))
        db.alter_column('restaurants_referingsite', 'restaurant_id', orm['restaurants.referingsite:restaurant'])
        
        # Changing field 'Hours.restaurant'
        # (to signature: models.ForeignKey(orm['restaurants.Restaurant']))
        db.alter_column('restaurants_hours', 'restaurant_id', orm['restaurants.hours:restaurant'])
        
        # Changing field 'Rating.restaurant'
        # (to signature: models.ForeignKey(orm['restaurants.Restaurant']))
        db.alter_column('restaurants_rating', 'restaurant_id', orm['restaurants.rating:restaurant'])
        
        # Changing field 'Rating.user'
        # (to signature: models.ForeignKey(orm['auth.User']))
        db.alter_column('restaurants_rating', 'user_id', orm['restaurants.rating:user'])
        
        # Deleting unique_together for [name] on Restaurant.
        db.delete_unique('restaurants_restaurant', ['name'])
        
    
    
    models = {
        'auth.group': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'restaurants.hours': {
            'close_time': ('django.db.models.fields.TimeField', [], {}),
            'day': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'open_time': ('django.db.models.fields.TimeField', [], {}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['restaurants.Restaurant']"})
        },
        'restaurants.menuitem': {
            'bad_info': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_available': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'last_mod': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2009, 7, 28, 2, 13, 54, 11930)', 'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['restaurants.Restaurant']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'restaurants.rating': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['restaurants.Restaurant']"}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'restaurants.referingsite': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['restaurants.Restaurant']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'unique': 'True'})
        },
        'restaurants.restaurant': {
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_mod': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'}),
            'long': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True'}),
            'phone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        }
    }
    
    complete_apps = ['restaurants']
