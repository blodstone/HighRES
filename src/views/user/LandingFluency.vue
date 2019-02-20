<template>
    <div class="document">
        <!-- eslint-disable -->
        <h1 align="center">
            Please Read This Thoroughly Before You Consent!
        </h1>
        <p>Your task is to assess the <strong>quality</strong> of an English summary. There are at most 8 sentences that need to be evaluated separately. The task should be possible to complete in less than <strong>3 minutes</strong>.</p>
        <hr/>
        <p><strong>You have to assess a summary on two aspects:</strong></p>
        <blockquote>
             The summary is <strong>clear</strong>.
        </blockquote>
        <p><strong>Explanation:</strong> The summary is easy to read, with no difficulties in identifying the referents of the noun phrases or understanding the meaning of the sentence. Every noun/place/event should be well-specified.</p>
        <blockquote>
            The summary is <strong>grammatically</strong> correct.
        </blockquote>
        <p><strong>Explanation:</strong> There is no obviously ungrammatical sentences,
                                    e.g.,missing components, unrelated fragments or any other
                                    grammar-related problem that makes the
                                    text difficult to read.</p>
        <p>An example assessment of one bad summary in each aspect:</p>
        <blockquote>
            <strong>Lack of clarity</strong><br/>
          <a class="highlight">He</a>, born 2 May 1975, is a English retired professional footballer and current President of Inter Miami CF since .
          <p><strong>Explanation:</strong> The person that is higlighted is not specified which reduce the clarity of the sentence.</p>
        </blockquote>
       <blockquote>
            <strong>Grammatically wrong</strong><br/>
          David Robert Joseph Beckham, born 2 May 1975, <a class="highlight">are a</a> English retired professional footballer and current <a class="highlight">current</a> President of Inter Miami CF.
         <p><strong>Explanation:</strong> The highlighted words are grammatically wrong.</p>
        </blockquote>
        <p>You will be scoring each summary sentence by stating how strongly you agree or disagree using a slider from scale 1 (strong disagreement) to 100 (strong agreement).</p>
        <hr />
        <h4><strong>Sanity Check</strong></h4>
      <p>We have inserted <strong>an obviously bad and good summaries</strong> in between a real summaries. Any submission that failed to recognize the bad and good summaries and give them a suitable scores (the bad summary should has a lower score than good summary) will be <strong>rejected.</strong></p>
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
