<!--
Home page loaded by Admin
-->
<template>
    <div class="hero is-primary is-large">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">
            Welcome to HArnESS (Highlight-bAsed Evaluation of Single document Summarization)!
          </h1>
          <h2 class="subtitle">
            An open source manual evaluation software for summarization!
          </h2>
        </div>
      </div>
    </div>
</template>

<script lang="ts">
import { Vue } from 'vue-property-decorator';

export default class Home extends Vue {}
</script>

<style scoped>
.title {
  font-size: 3rem;
}
.subtitle {
  font-size: 1.5rem;
}
</style>
