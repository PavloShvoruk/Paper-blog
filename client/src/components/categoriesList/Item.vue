<template>
  <div class="title">
    <h4>
      <a>{{ categoryName }}</a>
    </h4>
  </div>
</template>
<style scoped>
a {
  cursor: pointer;
}
</style>


<script>
export default {
  name: "category-item",
  props: {
    categoryName: String
  }
};
</script>