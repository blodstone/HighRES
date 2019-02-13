<template>
    <div class="document">
        <!-- eslint-disable -->
        <h1 align="center">
            Please Read This Thoroughly Before You Consent!
        </h1>
        <p>Your task is to assess the <strong>fluency</strong> of a single summary sentence. There are at most 8 summaries that need to be evaluated. The task should be possible to complete in less than <strong>3 minutes</strong>.</p>
        <hr/>
        <p><strong>You have to assess the summary on three metrics:</strong></p>
        <blockquote>
             The summary has a <strong>clear reference</strong>.
        </blockquote>
        <p><strong>Meaning:</strong> All the the referents of nounphrases in this summary are easily identifiable, i.e.: All the nouns, pronouns or personal names are well-specified?.</p>
        <blockquote>
            The summary is <strong>grammatically</strong> correct.
        </blockquote>
        <p><strong>Meaning:</strong> There any no obviously ungrammatical sentences,
                                    e.g.,missing components, unrelated fragments or any other
                                    grammar-related problem that makes the
                                    text difficult to read.</p>
        <blockquote>
            The summary has no noticeable <strong>formatting problem</strong>
        </blockquote>
        <p><strong>Meaning:</strong> There are no datelines, system-internal
                              formatting or capitalization errors that can make the reading
                              of the summary difficult.</p>

        <p>An example assessment of one bad summary in each category:</p>
        <blockquote>
            <strong>No Clear Reference</strong><br/>
          <a class="highlight">He</a>, born 2 May 1975, is a English retired professional footballer and current President of Inter Miami CF since .
        </blockquote>
       <blockquote>
            <strong>Grammatically wrong</strong><br/>
          David Robert Joseph Beckham, born 2 May 1975, <a class="highlight">are a</a> English retired professional footballer and current <a class="highlight">current</a> President of Inter Miami CF.
        </blockquote>
        <blockquote>
            <strong>Formatting Problem</strong><br/>
          David Robert Joseph Beckham, born <a class="highlight">02051975</a>, is a English retired <a class="highlight">&lt;UNK&gt;</a> footballer and current President of Inter Miami CF.
        </blockquote>
        <p>You will be scoring each summary sentence by stating how strongly you agree or disagree using a slider from scale 1 (strong disagreement) to 100 (strong agreement).</p>
        <hr />
        <h4><strong>Sanity Check</strong></h4>
        <p>We have inserted an obviously bad and good fake summaries in between a real summaries. Any submission that failed to recognize the bad and good fake summaries and give them a suitable scores will be <strong>rejected.</strong></p>
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
