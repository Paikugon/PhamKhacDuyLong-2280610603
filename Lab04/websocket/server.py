import random
import tornado.ioloop
import tornado.web
import tornado.websocket

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    clients = set()

    def open(self):
        self.clients.add(self)
        print("WebSocket opened")

    def on_message(self, message):
        print(f"Message received: {message}")
        # Broadcast the message to all connected clients
        for client in self.clients:
            if client != self:
                client.write_message(message)

    def on_close(self):
        self.clients.remove(self)
        print("WebSocket closed")
        
    @classmethod
    def send_message(cls, message):
        for client in cls.clients:
            client.write_message(message)
            
class RandomWordSelector:
    def __init__(self, words):
        self.words = words

    def get_random_word(self):
        return random.choice(self.words)
    
def main():
    app = tornado.web.Application([
        (r"/websocket/", WebSocketHandler),
    ])
    app.listen(8888)
    io_loop = tornado.ioloop.IOLoop.current()
    word_selector = RandomWordSelector(["apple", "banana", "cherry", "date"])
    
    periodic_callback = tornado.ioloop.PeriodicCallback(
        lambda: WebSocketHandler.send_message(word_selector.get_random_word()), 3000
    )
    periodic_callback.start()
    io_loop.start()
    
if __name__ == "__main__":
    print("Starting WebSocket server")
    main()