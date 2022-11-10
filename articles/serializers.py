from rest_framework import serializers
from articles.models import Article

class ArticlesSerializer(serializers.ModelSerializer):#어떻게 생겼는지 가져와라
    class Meta:
        model = Article
        fields = '__all__'

print(ArticlesSerializer)
print("--------------ArticlesSerializer----------------")

# 주먹밥(Article class)
# 손으로 밥,마요네즈,참치 손으로 둥글게 만든다. articles = Article.objects.all()
# 삼각형으로 만들고 싶은데
### seriallizer라는 삼각형틀 (4-7번줄 ArticlesSerializer)
# 주먹밥들을 안에 넣는다. ArticlesSerializer(articles, many=True)
# 삼각형안에 삼각김밥이 나옴.