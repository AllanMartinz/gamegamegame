from code.Const import WIN_WIDTH
from code.enemy import Enemy
from code.enemyShot import EnemyShot
from code.entity import Entity
from code.playerShot import PlayerShot


class EntityMediator:

 #__metodo quando usado o __ em um metodo o transformara em private
    @staticmethod
    def __verify_collision_window(ent: Entity):
        #se foi isntaciado o tipo Enemy
        if isinstance(ent, Enemy):
            #caso a entidade passar de zero no retangulo  da direita
            if ent.rect.right <= 0:
                # a vida sera 0
                ent.health = 0
        #caso o tiro passar do cenario sera destuido
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.left <= 0:
                ent.health = 0
        pass

    #verifica a colisao
    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

    #verifica a vida
    @staticmethod
    def verify_health(entity_list: list[Entity]):
        #para cada entidade em entity_list
        for ent in entity_list:
            #se a health dela for menor ou igual a 0
            if ent.health <= 0:
                #a entidade sera removida
                entity_list.remove(ent)
