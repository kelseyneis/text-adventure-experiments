import world, requests, relevance

class Character:

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

class DadJokeGuy(Character):
    def __init__(self):
        super().__init__(name="Dad Joke Guy", image="Sunflower.jpg", favor=10, damage=2, location_x=0, location_y=4)

    def converse(self):
        while input('       Wanna hear a joke?\n> ') != 'no':
            resp = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'text/plain'})
            if resp.status_code != 200:
                raise ApiError('GET /tasks/ {}'.format(resp.status_code))
            print(f"    {resp.text}")
            userInput = input()
            relevance_sentiment = relevance.joke_response_analyzer(resp.text, userInput)
            response_relevance = relevance_sentiment['relevance']
            sentiment = relevance_sentiment['sentiment']['compound']

            # TODO: make this fuzzy
            pleased_as_punch = (sentiment >= .8 and response_relevance >= .6)
            very_pleased = .3 <= sentiment < .8 and response_relevance >= .4
            concerned = sentiment >= .8 and response_relevance < .6
            non_plussed = .3 <= sentiment < .8 and response_relevance < .4
            hurt = sentiment < .3 and response_relevance < .4
            teased = sentiment < .3 and response_relevance >= .6

            if very_pleased:
                continue
            elif pleased_as_punch:
                print("     I knew you'd like it. You've always had a good sense of humor")
            elif non_plussed:
                break
            elif teased:
                print("     You little bugger you!")
            elif concerned:
                print("     Is everything alright? You seem preoccupied")
            elif hurt:
                print("     Well, that was just plain mean! Try to spread some cheer in this world...")
                break
        else:
            print("Alright, suit yourself. Don't forget to eat breakfast!")
