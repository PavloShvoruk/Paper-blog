<template>
  <div>
    <div v-for="(article, index) in articles" :key="index">
      <articleItem
        :id="article.id"
        :title="article.title"
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