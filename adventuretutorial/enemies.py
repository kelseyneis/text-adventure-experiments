import world, requests, relevance

class Enemy:

    """A base class for all enemies"""
    def __init__(self, name, image, favor, damage, location_x, location_y):
        """Creates a new enemy

        :param name: the name of the enemy
        :param favor: how much the character likes you
        :param damage: the damage the enemy does with each attack
        """

        self.name = name
        self.favor = favor
        self.location_x, self.location_y = (location_x, location_y)
        self.damage = damage
        self.image = image

    def is_alive(self):
        return self.favor > 0

    def converse(self):
        raise NotImplementedError()

class DadJokeGuy(Enemy):
    def __init__(self):
        super().__init__(name="Dad Joke Guy", image="Sunflower.jpg", favor=10, damage=2, location_x=0, location_y=4)

    def converse(self):
        while input('       Hey pumpkin, I have a new joke I think you\'ll like. Wanna hear it?\n> ') != 'no':
            resp = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'text/plain'})
            if resp.status_code != 200:
                # This means something went wrong.
                raise ApiError('GET /tasks/ {}'.format(resp.status_code))
            print(resp.text)
            userInput = input()
            if(userInput.lower() == 'haha'):
                self.favor += 5
                print("Dad is pleased that you liked his joke. New favor: ", self.favor)
            elif(relevance.joke_response_analyzer(resp.text, userInput) == 0):
                print('well fine')
        else:
            print('Alright, suit yourself. Don\'t forget to eat breakfast!')
