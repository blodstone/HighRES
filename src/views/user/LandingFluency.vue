<template>
    <div class="document">
        <!-- eslint-disable -->
        <h1 align="center">
            Please Read This Thoroughly Before You Consent!
        </h1>
        <p>Your task is to assess the <strong>quality</strong> of an English summary sentence. There are at most 8 sentences that need to be evaluated separately. The task should be possible to complete in less than <strong>3 minutes</strong>.</p>
        <hr/>
        <p><strong>You have to assess a summary on two aspects:</strong></p>
        <blockquote>
          1. The <strong>clarity</strong> of the summary.
        </blockquote>
        <p><strong>Explanation:</strong> The summary has to be easy to be understood. There should be no difficulties in identifying the referents of the noun phrases (every noun/place/event should be well-specified) or understanding the meaning of the sentence. </p>
        <blockquote>
          2. The <strong>fluency</strong> of the summary.
        </blockquote>
        <p><strong>Explanation:</strong> The summary should sound natural and has no grammar-related problem that makes the text difficult to read.</p>
        <p>The following are assessment of a bad summary according to each aspect:</p>
        <blockquote>
            <strong>Lack of clarity</strong><br/>
          <a class="highlight">He</a>, born 2 May 1975, is a English retired professional footballer and current President of Inter Miami CF since .
          <p><strong>Explanation:</strong> The person that is higlighted is not well-specified which reduce the clarity of the sentence.</p>
        </blockquote>
       <blockquote>
            <strong>Grammatically wrong</strong><br/>
          David Robert Joseph Beckham, born 2 May 1975, <a class="highlight">are a</a> English retired professional footballer and current <a class="highlight">current</a> President of Inter Miami CF.
         <p><strong>Explanation:</strong> The highlighted words are grammatically wrong.</p>
        </blockquote>
        <p>You will be scoring each summary sentence by stating how strongly you agree or disagree using a slider from scale 1 (strong disagreement) to 100 (strong agreement).</p>
        <hr />
        <h4><strong>Sanity Check</strong></h4>
      <p>We have inserted <strong>an obviously bad, mediocre and good summaries</strong> in between a real summaries. A bad summary has many grammatical mistakes and isn't fluent at all, a mediocre summary has some grammatical mistakes but still understandable, while a good summary has no grammatical mistakes and is fluent.</p>
      <p>Any submission that failed to recognize the bad, mediocre and good summaries with a suitable scores (bad < medium < good) will be <strong>rejected.</strong></p>
        <hr/>
        <p>There is a <strong>code</strong> that you have to copy and paste to Amazon platform at the end of the task.</p>

        <p>Thank you for reading this</p>
        <p>
            Do you consent for this information to be used
            anonymously for research purposes only?
        </p>
        <!-- eslint-enable -->
    </div>
</template>

<script>
export default {
  name: 'LandingInfRefMTurk',
};
</script>
<style scoped lang="scss">
h3 {
    margin-top: 2rem;
    margin-bottom: 3rem;
}
.document {
  font-family: 'Lora', serif;
  font-size: 1.1rem;
  line-height: 1.5rem;
  padding-left: 2rem;
  padding-right: 2rem;
  padding-bottom: 2rem;
}
.highlight {
  color: red;
}
</style>
