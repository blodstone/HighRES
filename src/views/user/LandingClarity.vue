<template>
    <div class="document">
        <!-- eslint-disable -->
        <h1 align="center">
            Please Read This Thoroughly Before You Consent!
        </h1>
        <p>Your task is to assess the <strong>clarity</strong> of an English summary sentence. A <strong>clear</strong> summary has to be easy to be understood. There should be no difficulties in identifying the referents of the noun phrases (every noun/place/event should be well-specified) or understanding the meaning of the sentence. </p>
      <p>There are at most 8 sentences that need to be evaluated separately. The task should be possible to complete in less than <strong>2 minutes</strong>.</p>
        <hr/>
        <p>The following are assessment of a bad summary according to each aspect:</p>
        <blockquote>
            <strong>Lack of clarity</strong><br/>
          <a class="highlight">He</a> is an English retired professional footballer and current President of Inter Miami CF.
          <p><strong>Explanation:</strong> The highlighted word is not well-specified (we don’t know who is the subject) which reduce the clarity of the sentence.</p>
        </blockquote>
        <p>You will be scoring each summary sentence by stating how strongly you agree or disagree using a slider from scale 1 (strong disagreement) to 100 (strong agreement).</p>
        <hr />
        <h4><strong>Sanity Check</strong></h4>
      <p>We have inserted <strong>an obviously bad, mediocre and good summaries</strong> in between a real summaries. A bad summary has no clarity at all, a mediocre summary has some part of the referents that are specified while others don't, while a good summary has good clarity.</p>
      <p>Any submission that failed to recognize the bad, mediocre and good summaries with a suitable scores (bad < mediocre < good) will be <strong>rejected.</strong></p>
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
