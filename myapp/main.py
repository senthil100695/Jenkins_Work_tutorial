import fire

def hello(name="Jenkins Senthil how are you"):
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)
