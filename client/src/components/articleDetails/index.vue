<template>
  <div class="card" style="width: 20rem;">
    <div class="card-header">{{$route.params.articleID }}</div>
    <div class="card-body">
      <h4 class="card-title">{{article.title}}</h4>
      <p class="card-text">{{ article.article_text }}</p>
    </div>
    <div class="card-footer">Footer</div>
  </div>
</template>
<style scoped>
.card {
  margin-top: 5rem;
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