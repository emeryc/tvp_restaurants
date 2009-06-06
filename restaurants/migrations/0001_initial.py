
from south.db import db
from django.db import models
from restaurants.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Restaurant'
        db.create_table('restaurants_restaurant', (
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField(max_length=60)),
            ('slug', models.SlugField(unique=True)),
            ('address1', models.CharField("Address Line 1", max_length=50)),
            ('address2', models.CharField("Address Line 2", max_length=50, blank=True)),
            ('city', models.CharField(max_length=60)),
            ('zipcode', models.CharField(max_length=10, blank=True)),
            ('phone', PhoneNumberField(blank=True)),
            ('website', models.URLField(blank=True)),
            ('user', models.ForeignKey(orm['auth.User'])),
            ('last_mod', models.DateTimeField(auto_now=True)),
            ('lat', models.FloatField(default=0, blank=True)),
            ('long', models.FloatField(default=0, blank=True)),
        ))
        db.send_create_signal('restaurants', ['Restaurant'])
        
        # Adding model 'MenuItem'
        db.create_table('restaurants_menuitem', (
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField(max_length=60)),
            ('category', models.CharField(max_length=60)),
            ('description', models.TextField()),
            ('price', models.DecimalField(max_digits=5, decimal_places=2)),
            ('user', models.ForeignKey(orm['auth.User'])),
            ('is_available', models.BooleanField(default=True)),
            ('restaurant', models.ForeignKey(orm.Restaurant)),
            ('bad_info', models.BooleanField(default=False)),
            ('last_mod', models.DateTimeField(default=datetime.datetime(2009, 6, 6, 15, 30, 32, 916684), auto_now=True)),
        ))
        db.send_create_signal('restaurants', ['MenuItem'])
        
        # Adding model 'ReferingSite'
        db.create_table('restaurants_referingsite', (
            ('id', models.AutoField(primary_key=True)),
            ('restaurant', models.ForeignKey(orm.Restaurant)),
            ('url', models.URLField(unique=True)),
        ))
        db.send_create_signal('restaurants', ['ReferingSite'])
        
        # Adding model 'Hours'
        db.create_table('restaurants_hours', (
            ('id', models.AutoField(primary_key=True)),
            ('restaurant', models.ForeignKey(orm.Restaurant)),
            ('day', models.CharField(max_length=3)),
            ('open_time', models.TimeField()),
            ('close_time', models.TimeField()),
        ))
        db.send_create_signal('restaurants', ['Hours'])
        
        # Adding model 'Rating'
        db.create_table('restaurants_rating', (
            ('id', models.AutoField(primary_key=True)),
            ('user', models.ForeignKey(orm['auth.User'])),
            ('restaurant', models.ForeignKey(orm.Restaurant)),
            ('score', models.IntegerField()),
        ))
        db.send_create_signal('restaurants', ['Rating'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Restaurant'
        db.delete_table('restaurants_restaurant')
        
        # Deleting model 'MenuItem'
        db.delete_table('restaurants_menuitem')
        
        # Deleting model 'ReferingSite'
        db.delete_table('restaurants_referingsite')
        
        # Deleting model 'Hours'
        db.delete_table('restaurants_hours')
        
        # Deleting model 'Rating'
        db.delete_table('restaurants_rating')
        
    
    
    models = {
        'restaurants.referingsite': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'restaurant': ('models.ForeignKey', ["orm['restaurants.Restaurant']"], {}),
            'url': ('models.URLField', [], {'unique': 'True'})
        },
        'restaurants.hours': {
            'close_time': ('models.TimeField', [], {}),
            'day': ('models.CharField', [], {'max_length': '3'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'open_time': ('models.TimeField', [], {}),
            'restaurant': ('models.ForeignKey', ["orm['restaurants.Restaurant']"], {})
        },
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'restaurants.rating': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'restaurant': ('models.ForeignKey', ["orm['restaurants.Restaurant']"], {}),
            'score': ('models.IntegerField', [], {}),
            'user': ('models.ForeignKey', ["orm['auth.User']"], {})
        },
        'restaurants.restaurant': {
            'address1': ('models.CharField', ['"Address Line 1"'], {'max_length': '50'}),
            'address2': ('models.CharField', ['"Address Line 2"'], {'max_length': '50', 'blank': 'True'}),
            'city': ('models.CharField', [], {'max_length': '60'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'last_mod': ('models.DateTimeField', [], {'auto_now': 'True'}),
            'lat': ('models.FloatField', [], {'default': '0', 'blank': 'True'}),
            'long': ('models.FloatField', [], {'default': '0', 'blank': 'True'}),
            'name': ('models.CharField', [], {'max_length': '60'}),
            'phone': ('PhoneNumberField', [], {'blank': 'True'}),
            'slug': ('models.SlugField', [], {'unique': 'True'}),
            'user': ('models.ForeignKey', ["orm['auth.User']"], {}),
            'website': ('models.URLField', [], {'blank': 'True'}),
            'zipcode': ('models.CharField', [], {'max_length': '10', 'blank': 'True'})
        },
        'restaurants.menuitem': {
            'bad_info': ('models.BooleanField', [], {'default': 'False'}),
            'category': ('models.CharField', [], {'max_length': '60'}),
            'description': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_available': ('models.BooleanField', [], {'default': 'True'}),
            'last_mod': ('models.DateTimeField', [], {'default': 'datetime.datetime(2009, 6, 6, 15, 30, 33, 513054)', 'auto_now': 'True'}),
            'name': ('models.CharField', [], {'max_length': '60'}),
            'price': ('models.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'restaurant': ('models.ForeignKey', ["orm['restaurants.Restaurant']"], {}),
            'user': ('models.ForeignKey', ["orm['auth.User']"], {})
        }
    }
    
    complete_apps = ['restaurants']
