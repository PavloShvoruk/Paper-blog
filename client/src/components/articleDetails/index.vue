<template>
  <div class="sm-6 md-8 lg-10 row flex-center paper">
    <article class="article">
      <h1 class="article-title">{{article.title}}</h1>
      <p class="article-meta">
        Written by
        <a href="#">Super User</a>
      </p>
      <p class="article-text">{{ article.article_text }}</p>
      <div class="row">
        <button>5 Comments</button>
      </div>
    </article>
  </div>
</template>
<style scoped>
.paper {
  margin-top: 5rem;
}
.paper p {
  text-indent: 1rem;
}
</style>


<script>
import ApiService from "../../ApiService.js";
export default {
  name: "article-details",
  data() {
    return {
      article: []
    };
  },
  async mounted() {
    try {
      this.article = await ApiService.getArticle(this.$route.params.articleID);
      console.log(this.article);
    } catch (error) {
      console.log(error.message);
    }
  }
};
</script>