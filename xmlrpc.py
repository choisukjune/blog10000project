from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo

wp = Client('http://csj107308.dothome.co.kr/xmlrpc.php', 'marketAdmin', 'tjrwns2482!@')
# wp.call(GetPosts())


# wp.call(GetUserInfo())

post = WordPressPost()
post.title = 'My new title'
post.content = 'This is the body of my new post.'
post.post_status = "publish"
post.terms_names = {
  'post_tag': ['test', 'firstpost'],
  'category': ['뉴스']
}
wp.call(NewPost(post))


