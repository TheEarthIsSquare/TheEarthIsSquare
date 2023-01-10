<template>
  <div id="course">
    <CourseInformationSection/>

    <QuoteBreakSection/>

    <LearnSection/>

    <LocationSection/>

    <OutcomesSection/>

    <FAQSection/>

    <CTASection/>
  </div>
</template>

<script lang="ts" setup>
import { useHead } from "#head";
import CourseInformationSection from "~/features/course/CourseInformationSection.vue";
import CTASection from "~/features/course/CTASection.vue";
import FAQSection from "~/features/course/FAQSection.vue";
import LearnSection from "~/features/course/LearnSection.vue";
import LocationSection from "~/features/course/LocationSection.vue";
import OutcomesSection from "~/features/course/OutcomesSection.vue";
import QuoteBreakSection from "~/features/course/QuoteBreakSection.vue";

useHead({
  title: "Course Details - The Earth Is Square // Think Outside The Square"
});
</script>

<style lang="scss" scoped>
#course {
  display: flex;
  flex-direction: column;
  margin-right: 0.6rem;
  gap: 0.6rem;
}
</style>