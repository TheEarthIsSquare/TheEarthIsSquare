<template>
  <div id="course">
    <CourseInformationSection />

    <QuoteBreakSection />

    <LearnSection />

    <LocationSection />

    <OutcomesSection />

    <FAQSection />

    <CTASection />
  </div>
</template>

<script lang="ts" setup>
import { useHead } from "#head";
import CourseInformationSection from "~/pages/course/features/CourseInformationSection.vue";
import CTASection from "~/pages/course/features/CTASection.vue";
import FAQSection from "~/pages/course/features/FAQSection.vue";
import LearnSection from "~/pages/course/features/LearnSection.vue";
import LocationSection from "~/pages/course/features/LocationSection.vue";
import OutcomesSection from "~/pages/course/features/OutcomesSection.vue";
import QuoteBreakSection from "~/pages/course/features/QuoteBreakSection.vue";

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