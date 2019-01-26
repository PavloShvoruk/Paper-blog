<template>
  <div>
    <div v-for="(article, index) in articles" :key="index">
      <articleItem
        :title="article.title"
        :articleText="article.article_text"
        :publishedAt="article.published_at"
        :author="article.author"
        :category="article.board.name"
      />
    </div>
  </div>
</template>

<script>
import articleItem from "./Item";
export default {
  components: {
    articleItem
  },
  name: "articles-list",
  props: ["articles"]
};
</script>