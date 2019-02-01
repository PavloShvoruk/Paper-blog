<template>
  <div class="card" style="width:100%;">
    <div class="card-body">
      <h3 class="card-title">{{ title }}</h3>
      <h5 class="card-subtitle">Posted on {{ publishedAt }}</h5>
      <h5 class="card-subtitle">Author: {{ author.username }}</h5>
      <button>Let me go here!</button>
    </div>
  </div>
</template>
<style scoped>
.card {
  margin-bottom: 1rem;
}
</style>

<script>
export default {
  name: "Article-item",
  props: ["title", "publishedAt", "author", "category"]
};
</script>