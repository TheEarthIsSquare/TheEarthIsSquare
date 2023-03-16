<template>
  <div id="course">
    <CourseInformationSection/>

    <OutcomesSection/>

    <QuoteBreakSection/>

    <template v-if="isDesktop">
      <LearnSection/>

<!--      <LocationSection/>-->

      <FAQSection/>

      <CTASection/>
    </template>
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
import { useScreen } from "~/hooks/useScreen";

useHead({
  title: "Course Details - The Earth Is Square // Think Outside The Square"
});

const { isDesktop } = useScreen();
</script>

<style lang="scss" scoped>
#course {
  display: flex;
  flex-direction: column;
  margin-right: 0.6rem;
  gap: 0.6rem;
}
</style>