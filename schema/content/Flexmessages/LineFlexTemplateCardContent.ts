// Contents/FlexMessages/line-flex-template-card-content.ts
import { z } from "zod";
import { LineActionContent } from "./LineActionContent"; // 依專案實際路徑調整

// ── 共用工具 ───────────────────────────────────────────────
const AltTextNonBlank = z
  .string()
  .refine((s) => /\S/.test(s), "AltText 不能為空白字元");

// Parameter 基底（兩種容器都會用到）
const FlexMessageParameterBase = z.object({
  Type: z.enum(["use_expression", "plain", "variable"]),
  // Value 可為字串/數字/布林/陣列/物件（支援模板字串與表達式）
  Value: z.union([z.string(), z.number(), z.boolean(), z.array(z.any()), z.record(z.any())]),
  Options: z.record(z.any()).optional(),
});

// 陣列寫法：內含 Name 欄位
const FlexMessageParameter = FlexMessageParameterBase.extend({
  Name: z.string().min(1),
});

// 字典寫法：key 作為 Name，value 不含 Name
const FlexMessageParameterNoName = FlexMessageParameterBase;

// 允許兩種 Parameters 形式：Array 或 Record
const FlexMessageParameters = z.union([
  z
    .array(FlexMessageParameter)
    .superRefine((arr, ctx) => {
      const seen = new Set<string>();
      for (const p of arr) {
        if (seen.has(p.Name)) {
          ctx.addIssue({
            code: z.ZodIssueCode.custom,
            message: `Parameters 中的 Name 不可重複：${p.Name}`,
          });
        }
        seen.add(p.Name);
      }
    }),
  z.record(FlexMessageParameterNoName),
]);

// ── 主體 Schema ─────────────────────────────────────────────
export const LineFlexTemplateCardContent = z.object({
  Type: z.literal("line.flex.card.template"),
  AltText: AltTextNonBlank,
  TemplateId: z.string().min(1),
  Content: z.string().min(1), // Flex JSON（字串形式）。若需強化，可加 refine 檢查 JSON.parse 可行。

  Parameters: FlexMessageParameters.optional(),
  QuickReply: z.array(LineActionContent).optional(),
});

// 型別匯出
export type TLineFlexTemplateCardContent = z.infer<typeof LineFlexTemplateCardContent>;
