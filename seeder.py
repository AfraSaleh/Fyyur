from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fyyur import Venue, Show, Artist
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(bind=engine)
engine = create_engine(DB_PATH)
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
# data
venue = Venue(id="1", name="The Musical Hop", city="San Francisco", state="CA", address="1015 Folsom Street" , phone="123-123-1234",
	image_link="https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60", facebook_link="https://www.facebook.com/TheMusicalHop", )
session.add(venue)
session.commit()
artist = Artist(id="4", name="Guns N Petals", city="San Francisco", state="CA", phone="326-123-5000" , genres="Rock n Roll", image_link="https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",facebook_link="https://www.facebook.com/GunsNPetals",)
session.add(artist)
session.commit()
show1 = Show(venue=venue, artist=artist, start_time="2019-05-21T21:30:00.000Z")
session.add(show1)
session.commit()