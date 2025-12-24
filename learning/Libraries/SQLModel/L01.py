# first map sql tables


# creating a sqlmodel
from sqlmodel import Field, Session, SQLModel, create_engine, select  # Session and create_engine needed to write to database


class Hero(SQLModel, table=True):  # class hero is a sql model equivalent to a sql table
    # class attributes are equivalent to each column of the table
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    secret_name: str
    age: int | None = None 


# creating rows
hero_1 = Hero(name='<NAME>', secret_name='<Name>', age=18)
hero_2 = Hero(name='Deadpond', secret_name='James Walrich')
hero_3 = Hero(name='Fran Pire', secret_name='Francois Andrews', age=70)
hero_4 = Hero(name='The Knight', secret_name='Willy Macantosh', age=18)
hero_5 = Hero(name='Kitty', secret_name='Jane Sliven', age=23)

engine = create_engine('sqlite:///hero.db')

SQLModel.metadata.create_all(engine)

heroes_to_add = [hero_5]

with Session(engine) as session:
    for hero in heroes_to_add:

        # 1. Search for a hero with this name
        statement = select(Hero).where(Hero.name == hero.name)
        existing_hero = session.exec(statement).first()

        # 2. Decision logic
        if not existing_hero:
            session.add(hero)
            print(f'Adding {hero.name} to the database')
        else:
            print(f'skipping {hero.name}: Already exists')
        # 3. finalize
        session.commit()

    # Reading the data immediately after
    statement = select(Hero)
    results = session.exec(statement)
    for hero in results:
        print(hero)
