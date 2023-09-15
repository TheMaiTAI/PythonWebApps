from django.views.generic import TemplateView

class HeroListView(TemplateView):
    template_name = 'index.html'
    
class HeroFirstDetailView(TemplateView):  
        
    template_name = 'hero.html'
    
    def get_context_data(self, **kwargs):
        return {
            
            'title': 'The Shield Hero',
            'name': 'Naofumi Iwatani',
            'age': '20 years old',
            'weapon': 'Legendary Shield',
            'strength1': 'Cunning Merchant',
            'strength2': 'Pragmatic',
            'strength3': 'Common Sense',
            'weak1': 'Extremely Distrustful',
            'weak2': 'Lack of Empathy',
            'weak3': 'Poor Reputation',
            'image': '/static/images/naofumi.jpg',
            'type': 'shield'
            
            }
    
class HeroSecondDetailView(TemplateView):  
        
    template_name = 'hero.html'
    
    def get_context_data(self, **kwargs):
        return {
            
            'title': 'Phantom',
            'name': 'Danny Fenton',
            'age': '14 years old',
            'weapon': 'Ghost Powers',
            'strength1': 'Varied Powerset',
            'strength2': 'Near-impossible for normal humans to hurt',
            'strength3': 'Very clever and quick-witted',
            'weak1': 'Is a teenager',
            'weak2': 'Very petty and quick to anger',
            'weak3': 'Lives with ghost hunters',
            'image': '/static/images/danny.jpeg',
            'type': 'ghost'
            
            }
    
class HeroThirdDetailView(TemplateView):  
        
    template_name = 'hero.html'
    
    def get_context_data(self, **kwargs):
        return {
            
            'title': 'Joker, Leader of the Phantom Thieves',
            'name': 'Ren Amamiya / Akira Kurusu',
            'age': '16 years old',
            'weapon': 'Dagger / Pistol / Magic',
            'strength1': 'Acrobatic',
            'strength2': 'Very Charismatic',
            'strength3': 'Power level is almost directly proportional with the strength of his convictions',
            'weak1': 'Is currently on probation and watched very closely by the police and other adults',
            'weak2': 'Has a strict, cat-enforced curfew',
            'weak3': 'Impulsive and prone to showing off',
            'image': '/static/images/joker.jpg',
            'type': 'thief'
            
            }