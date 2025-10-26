def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Elaichi Chai"

# for chai in serve_chai():
#     print(chai)

# print(next(serve_chai()));  
# print(next(serve_chai()));  
# print(next(serve_chai()));  

chai = serve_chai()

print(next(chai))
print(next(chai))
print(next(chai))