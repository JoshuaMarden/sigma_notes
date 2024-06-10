___

[excalidraw](https://link.excalidraw.com/l/6gPaBlSh8PG/2KH3SWjx6Ng)
#### Workshop Pre-Work

__"What is REST"?
 - A uniform way to arrange an API so it can be accessed and sends readable data in response to known requests 

__"Why is it useful"
- So you don't have to learn a new system every time you contact an API, and programmers don't have to reinvent the wheel when implementing the API. Communication follows logical, consistent rules.

 __REST API Characteristics__

1. **Uniform Interface**: REST APIs use a consistent way to interact with resources. This means that the way to access, manipulate, and represent resources is standardized.
    
2. **Client-Server**: REST separates the user interface concerns (client) from data storage concerns (server), allowing each to evolve independently.
    
3. **Stateless**: Each request from the client to the server must contain all the information needed to understand and process the request, ensuring that no client context is stored on the server between requests.
    
4. **Cacheable**: Responses from the server can be explicitly marked as cacheable or non-cacheable to improve performance and reduce the load on the server (Caching is storing data near a user).
    
5. **Layered System**: REST architecture allows for an application to be composed of hierarchical layers by enforcing a layered system constraint. (Basically encapsulation - client doesn't care how API is structured)