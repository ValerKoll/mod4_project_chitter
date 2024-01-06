from lib.post import Post

class Post_repository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM posts')
        list_to_return = []
        for row in rows:
            post = Post(row['id'], row['title'], row['content'], row['user_id'], row['time_stamp'],)
            list_to_return.append(post)
        if len(list_to_return):
            return list_to_return

    def find(self, post_id):
        rows = self._connection.execute(
            'SELECT * from posts WHERE id = %s', [post_id]
            )
        # TODOs: Implement error checks insted of IF
        if rows:
            row = rows[0]
            post = Post(row['id'], row['title'], row['content'], row['user_id'], row['time_stamp'],)
            if post.is_valid():
                return (True, post)
            return (False, 'Stored values not valid')
        return (False, "Post not found")