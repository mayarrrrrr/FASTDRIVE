from fdmodels import create_engine,Base,sessionmaker

engine = create_engine("sqlite:///fastdrive.db")
Base.metadata.create_all(engine)
    
session = sessionmaker(bind=engine)
mysession = session()