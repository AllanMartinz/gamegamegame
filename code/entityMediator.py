from code.Const import WIN_WIDTH
from code.enemy import Enemy
from code.enemyShot import EnemyShot
from code.entity import Entity
from code.player import Player
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

    #verifica se ouve colisão
    @staticmethod
    #sera entre duas entidades ent1 e ent2 e a valid_collision sempre sera False so ate a colisão
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        #caso o Enemy atingir o PlayerShot a valid_collision sera true
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        # caso o Enemy atingir o PlayerShot a valid_collision sera true
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        # caso o EnemyShot atingir o Player a valid_collision sera true
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        # caso o EnemyShot atingir o Player a valid_collision sera true
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction: #valid_interraction == True
            if (ent1.rect.right >= ent2.rect.left
                    and ent1.rect.left <= ent2.rect.right
                    and ent1.rect.bottom <= ent2.rect.top
                    and ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    #verifica a colisao
    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Player1Shoot':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score
        if enemy.last_dmg == 'Player2Shoot':
            for ent in entity_list:
                if ent.name == 'Player2':
                    ent.score += enemy.score
        pass


    #verifica a vida
    @staticmethod
    def verify_health(entity_list: list[Entity]):
        #para cada entidade em entity_list
        for ent in entity_list:
            #se a health dela for menor ou igual a 0
            if ent.health <= 0:
                #a entidade sera removida
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)
