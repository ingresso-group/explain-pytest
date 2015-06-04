from django.db import models


class Animal(models.Model):
    color = models.CharField(max_length=64) 
    age = models.IntegerField() 
    name = models.CharField(max_length=64)

    class Meta:
        abstract = True


class Dog(Animal):
    OPTIMAL_BELLY_RUBS = 10
    belly_rubs_today = models.IntegerField()

    @property
    def happiness(self):
        return (belly_rubs_today / self.OPTIMAL_BELLY_RUBS) * 100


class Cat(Animal):
    DAYS_FOR_PLAN_TO_COME_INTO_EFFECT = 7
    evil_plans = models.IntegerField()
    arch_enemy = models.ForeignKey(Dog, blank=True, null=True)
    enemies = models.ManyToManyField(Dog)
    
    @property
    def days_to_world_take_over(self):
        return self.evil_plans * self.DAYS_FOR_PLAN_TO_COME_INTO_EFFECT

    def kill_enemies(self):
        if self.arch_enemy:
            self.arch_enemy.delete()
        for enemy in self.enemies:
            enemy.delete()
        return 'MUHAHAHAHAHAH!'

