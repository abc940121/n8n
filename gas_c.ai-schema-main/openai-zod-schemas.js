import { z } from "zod";
import { zodResponseFormat } from "openai/helpers/zod";

// ==========================================
// Rule System Schemas (基於 Rules/*.md)
// ==========================================

// Base Rule Schema (所有規則的基礎)
const BaseRuleCore = z.object({
  Type: z.string().describe("規則類型"),
});

// Text Rule Schema (基於 Rules/TextRule.md)
const TextRule = BaseRuleCore.extend({
  Type: z.literal("text").describe("規則類型：text"),
  Condition: z.enum([
    "startwith", "startWith", "start_with",
    "endwith", "endWith", "end_with", 
    "contain", "exactly", "equal", "==",
    "is_null", "is_null_or_empty", "isnull", "isnullorempty", "isNull", "isNullOrEmpty"
  ]).describe("文字判斷條件"),
  Value: z.string().optional().describe("期望的輸入"),
  IgnoreCase: z.boolean().default(false).describe("是否忽略大小寫"),
  IsNegative: z.boolean().default(false).describe("是否為否定條件")
});

// Regex Rule Schema (基於 Rules/RegexRule.md)
const RegexRule = BaseRuleCore.extend({
  Type: z.literal("regex").describe("規則類型：regex"),
  Pattern: z.string().optional().describe("Regex Pattern"),
  IgnoreCase: z.boolean().default(false).describe("是否忽略大小寫"),
  IsNegative: z.boolean().default(false).describe("是否為否定條件")
});

// Integer Rule Schema (基於 Rules/IntegerRule.md)
const IntegerRule = BaseRuleCore.extend({
  Type: z.literal("integer").describe("規則類型：integer"),
  Condition: z.enum([
    "IsInteger", "is_zero", "iszero", "isZero",
    "==", "!=", ">", ">=", "<", "<=",
    "max", "min", "between"
  ]).describe("整數判斷條件"),
  Value: z.number().int().optional().describe("期望的數值"),
  Value2: z.number().int().optional().describe("期望的數值2（僅between時使用）"),
  IsNegative: z.boolean().default(false).describe("是否為否定條件")
});

// Float Rule Schema (基於 Rules/FloatRule.md)
const FloatRule = BaseRuleCore.extend({
  Type: z.literal("float").describe("規則類型：float"),
  Condition: z.enum([
    "is_zero", "iszero", "isZero",
    "==", "!=", ">", ">=", "<", "<=",
    "max", "min", "between"
  ]).describe("浮點數判斷條件"),
  Value: z.number().optional().describe("期望的數值"),
  Value2: z.number().optional().describe("期望的數值2（僅between時使用）"),
  IsNegative: z.boolean().default(false).describe("是否為否定條件")
});

// Boolean Rule Schema (基於 Rules/BooleanRule.md)
const BooleanRule = BaseRuleCore.extend({
  Type: z.literal("boolean").describe("規則類型：boolean"),
  Condition: z.enum([
    "is_valid", "isvalid", "isValid",
    "is_true", "istrue", "isTrue",
    "is_false", "isfalse", "isFalse"
  ]).describe("布林判斷條件"),
  TruePatterns: z.array(z.string()).optional().describe("符合True的文字模式"),
  FalsePatterns: z.array(z.string()).optional().describe("符合False的文字模式"),
  IsNegative: z.boolean().default(false).describe("是否為否定條件")
});

// JsonPath Rule Schema (基於 Rules/JsonPathRule.md)
const JsonPathRule = BaseRuleCore.extend({
  Type: z.literal("jsonpath").describe("規則類型：jsonpath"),
  JsonPath: z.string().describe("JsonPath，指定要驗證的目標"),
  Rule: z.lazy(() => BaseRule).describe("指定要驗證的目標的驗證規則")
});

// Composite Rule Schema (基於 Rules/CompositeRule.md)
const CompositeRule = BaseRuleCore.extend({
  Type: z.literal("composite").describe("規則類型：composite"),
  Condition: z.enum(["and", "or"]).default("and").describe("複合規則判斷條件"),
  Rules: z.array(z.lazy(() => BaseRule)).min(1).describe("子規則陣列"),
  IsNegative: z.boolean().default(false).describe("是否為否定條件")
});

// DateTime Rule Schema (基於 Rules/DateTimeRule.md)
const DateTimeRule = BaseRuleCore.extend({
  Type: z.literal("datetime").describe("規則類型：datetime"),
  Condition: z.enum([
    "is_valid", "isvalid", "isValid",
    "is_today", "istoday", "isToday",
    "is_same_date", "issamedate", "isSameDate",
    "before", "after", "between", "cron"
  ]).default("is_valid").describe("日期時間判斷條件"),
  Patterns: z.array(z.string()).optional().describe("自訂日期時間格式"),
  Value: z.string().optional().describe("期望的日期時間"),
  Value2: z.string().optional().describe("期望的日期時間2（僅between時使用）"),
  Expression: z.string().optional().describe("Cron Expression（僅cron時使用）")
});

// Evaluate Expression Rule Schema (基於 Rules/EvaluateExpressionRule.md)
const EvaluateExpressionRule = BaseRuleCore.extend({
  Type: z.literal("evaluate_expression").describe("規則類型：evaluate_expression"),
  ExpressionType: z.enum(["csharp", "javascript"]).default("csharp").describe("使用的公式類型"),
  Expression: z.string().describe("自訂要驗證的公式，回傳值必須為bool")
});

// Intent Rule Schema (基於 Rules/IntentRule.md)
const IntentRule = BaseRuleCore.extend({
  Type: z.literal("intent").describe("規則類型：intent"),
  Intent: z.string().describe("意圖的類型"),
  Score: z.number().min(0).max(1).default(0.8).describe("信心指數")
});

// Variable Rule Schema (基於 Rules/VariableRule.md)
const VariableRule = BaseRuleCore.extend({
  Type: z.literal("variable").describe("規則類型：variable"),
  Rule: z.lazy(() => BaseRule).describe("指定要驗證的目標的驗證規則"),
  JsonPath: z.string().describe("Variable JsonPath，指定要驗證的目標")
});

// Union of all rule types
const BaseRule = z.union([
  TextRule,
  RegexRule, 
  IntegerRule,
  FloatRule,
  BooleanRule,
  JsonPathRule,
  CompositeRule,
  DateTimeRule,
  EvaluateExpressionRule,
  IntentRule,
  VariableRule
]).describe("基礎規則（所有規則類型的聯集）");

// ==========================================
// Node Action Schema (基於 Actions/NodeAction.md)
// ==========================================
const NodeAction = z.object({
  _Id: z.string().optional().describe("Action ID"),
  Name: z.string().optional().describe("Action 的名稱或敘述"),
  Rules: z.array(BaseRule).describe("Node 轉換規則"),
  Type: z.enum(["and", "or", "intersection", "union", "none", "otherwise"])
    .default("none")
    .describe("多組規則的判斷"),
  Priority: z.number().min(0).max(100).describe("Action的優先順序，範圍 0 ~ 100"),
  NextNodeId: z.string().describe("符合條件時，轉換到下一個 Node")
});

// ==========================================
// Variable Action Schema (基於 Variables/VariableAction.md)
// ==========================================
const VariableAction = z.object({
  _Id: z.string().optional().describe("Variable Action ID"),
  Type: z.enum([
    "variable.set",
    "variable.remove", 
    "variable.remove.all"
  ]).describe("變數操作類型"),
  TriggerType: z.enum([
    "before_node",
    "retry_prompt", 
    "after_node"
  ]).default("after_node").describe("執行時間點"),
  Variable: z.string().optional().describe("變數名稱"),
  VariableType: z.enum([
    "global",
    "flow",
    "node"
  ]).default("global").describe("變數存取類型"),
  AssignValue: z.any().optional().describe("指派值"),
  AssignValueType: z.enum([
    "string",
    "string.json",
    "string.plain",
    "number",
    "boolean", 
    "object",
    "array",
    "variable",
    "evaluate_expression",
    "evaluate_csharp_expression",
    "evaluate_javascript_expression"
  ]).optional().describe("指派類型")
});

// ==========================================
// Base Dialog Node Schema (基於 Nodes/BaseDialogNode.md)
// ==========================================
const DiagramData = z.object({
  position: z.object({
    x: z.number(),
    y: z.number()
  }).describe("節點位置"),
  size: z.object({
    width: z.number(),
    height: z.number()
  }).describe("節點大小")
}).optional().describe("圖表資料");

const BaseDialogNode = z.object({
  Id: z.string().describe("Node ID (唯一)"),
  Name: z.string().optional().describe("Node 名稱"),
  Description: z.string().optional().describe("Node 描述"),
  Type: z.enum([
    // Send Message
    "send.message",
    "send.event", 
    "send.carousel",
    "typing.message",
    // Prompt
    "prompt.text",
    "prompt.card",
    "prompt.adaptivecard",
    // QA/NLU
    "qa.regex",
    "qa.luis",
    "qa.gssai",
    "qa.gssqa",
    // AI Services
    "ai.azure_openai_chat",
    // Flow Control
    "flow.begin",
    "flow.module.begin",
    "flow.switch",
    "flow.end.current",
    "flow.end.all",
    "flow.module.end",
    // Variable
    "variable",
    // External Services
    "request.raw",
    "request.json",
    "request.form",
    "request.parallel",
    "request.multicast",
    "request.binary",
    // Trace
    "trace",
    // Custom
    "custom.dialog",
    "function"
  ]).describe("Node 類型"),
  Actions: z.array(NodeAction).min(1).describe("Node 轉換行為 (至少一個)"),
  VariableActions: z.array(VariableAction).optional().describe("處理自訂變數"),
  Delay: z.number().min(0).max(3000).default(0).describe("延遲執行時間，範圍：0 ~ 3000 毫秒"),
  DiagramData: DiagramData
});

// ==========================================
// AI Chat Schemas
// ==========================================

// AI Chat Message Schema (基於 BaseAIChat.md)
const AIChatMessage = z.object({
  Role: z.enum(["system", "user", "assistant", "tool"]).describe("角色：system（系統）、user（使用者）、assistant（Bot）、tool（Tool Calling）"),
  Content: z.string().describe("訊息內容")
});

// Base AI Chat Node Schema (基於 BaseAIChat.md，繼承自 BaseDialogNode)
const BaseAIChatNode = BaseDialogNode.extend({
  ChatMessageHistory: z.string().optional().describe("先前的訊息，請指定一個變數名稱。變數值需為一個 AIChatMessage[] 格式"),
  ChatMessages: z.array(AIChatMessage).describe("最新的訊息（Chat Completions API）")
});


// Azure OpenAI Chat Endpoint Schema (基於 AzureOpenAIChat.md)
const AOAIChatEndpoint = z.object({
  Url: z.string().describe("Endpoint Url"),
  DeploymentId: z.string().describe("在 Azure 中部署的模型名稱"),
  ApiKey: z.string().describe("Azure API Key")
});

// Azure OpenAI Chat Options Schema (基於 AzureOpenAIChat.md)
const AOAIChatOptions = z.object({
  Stream: z.boolean().default(true).describe("是否啟用 Chat Stream，預設值：true"),
  MaxTokens: z.number().int().optional().describe("最大使用的 Token 數，預設值：16（官方預設值）")
});

// Azure OpenAI Chat Node Schema (基於 AzureOpenAIChat.md，繼承自 BaseAIChat)
const AzureOpenAIChatNode = BaseAIChatNode.extend({
  Type: z.literal("ai.azure_openai_chat").describe("Node 類型：ai.azure_openai_chat"),
  Endpoint: AOAIChatEndpoint.describe("Azure Open AI Endpoint 設定"),
  Options: AOAIChatOptions.optional().describe("Chat Completions API 除了訊息之外的選項")
});

// ==========================================
// Custom Node Schemas (基於 Nodes/Custom/*.md)
// ==========================================

// Custom Dialog Parameter Schema (基於 CustomDialog.md)
const CustomDialogParameter = z.object({
  $Type: z.enum(["use_expression", "plain", "variable", "message_content"]).default("use_expression").describe("參數的類型，預設值：use_expression"),
  $Value: z.any().describe("參數的值")
});

// Custom Dialog Node Schema (基於 CustomDialog.md，繼承自 BaseDialogNode)
const CustomDialogNode = BaseDialogNode.extend({
  Type: z.literal("custom.dialog").describe("Node 類型：custom.dialog"),
  PluginId: z.string().describe("自訂對話的 Plugin ID (不得重複)"),
  DialogName: z.string().describe("執行 DLL檔所需的 Dialog 類別名稱"),
  Parameters: z.record(CustomDialogParameter).optional().describe("執行自訂對話所需的參數")
});

// Custom Function Argument Schema (基於 CustomFunction.md)
const CustomFunctionArgument = z.object({
  Name: z.string().describe("引數名稱，在函式程式碼中使用的變數名稱 (不得重複)"),
  Type: z.enum(["use_expression", "plain", "variable"]).describe("引數的類型"),
  Value: z.any().describe("引數的值")
});

// JavaScript Library Schema (基於 CustomFunction.md)
const JavaScriptLibrary = z.object({
  LocalLibs: z.array(z.string()).optional().describe("指定的本機 JavaScript 檔案，目錄固定為網站目錄下的 Packages/JavaScript"),
  RemoteLibs: z.array(z.string()).optional().describe("指定的 URL，加入從 CDN 上的JavaScript Library")
});

// Custom Function Node Schema (基於 CustomFunction.md，繼承自 BaseDialogNode)
const CustomFunctionNode = BaseDialogNode.extend({
  Type: z.literal("function").describe("Node 類型：function"),
  ScriptType: z.enum(["cs_script", "javascript"]).default("cs_script").describe("程式碼語言，預設值：cs_script"),
  Arguments: z.array(CustomFunctionArgument).optional().describe("函式執行所需要的引數"),
  ScriptCode: z.string().describe("程式碼"),
  JavaScriptLibs: JavaScriptLibrary.optional().describe("外部 JS 套件，限 ScriptType = javascript")
});

// ==========================================
// Flow Control Node Schemas (基於 Nodes/FlowControl/*.md)
// ==========================================

// Flow Control Argument Schema (基於 BeginFlow.md, BeginModuleFlow.md, SwitchFlow.md)
const FlowControlArgument = z.object({
  $Type: z.enum(["use_expression", "plain", "variable"]).default("use_expression").describe("引數的類型，預設值：use_expression"),
  $Value: z.any().describe("引數的值")
});

// Message Content Schema (簡化版，基於 Contents/MessageContent.md)
// Message Content Schema (基於 Contents/MessageContent.md)
const MessageContent = z.object({
  Type: z.enum([
    // 一般訊息
    "none", "text", "text.random", "random",
    // Web Chat 專用
    "event", "attachment", "trace",
    // 卡片訊息
    "hero.card", "signin.card", "animation.card", "receipt.card", "audio.card", "video.card",
    // Adaptive Card 訊息
    "adaptive.card", "adaptive.card.fact", "adaptive.card.list", "adaptive.card.grid", 
    "adaptive.card.form", "adaptive.card.template", "adaptive.card.carousel_template",
    // 多個卡片
    "carousel",
    // LINE 專用
    "line.sticker", "line.flex", "line.flex.card.carousel", "line.flex.card.fact",
    "line.flex.card.list", "line.flex.card.grid", "line.flex.card.template", "line.flex.card.carousel_template",
    // Slack 專用
    "slack.blocks", "slack.blocks.list", "slack.blocks.form", "slack.blocks.template",
    // WeCom 專用
    "wecom.text", "wecom.card.fact", "wecom.card.button", "wecom.card.image",
    "wecom.card.choice", "wecom.card.dropdownlist", "wecom.card.template"
  ]).describe("訊息內容類型"),
  QuickReply: z.array(z.any()).optional().describe("快速回覆按鈕"),
  ChannelDataPayload: z.any().optional().describe("Channel Data Payload")
}).passthrough().describe("訊息內容");

// Begin Flow Node Schema (基於 BeginFlow.md，繼承自 BaseDialogNode)
const BeginFlowNode = BaseDialogNode.extend({
  Type: z.literal("flow.begin").describe("Node 類型：flow.begin"),
  Message: MessageContent.optional().describe("訊息內容（二擇一）"),
  Messages: z.array(MessageContent).optional().describe("多個訊息內容（二擇一）"),
  FlowId: z.string().describe("呼叫的 Flow ID"),
  Arguments: z.record(FlowControlArgument).describe("指派呼叫的 Flow 的流程變數")
});

// Begin Module Flow Node Schema (基於 BeginModuleFlow.md，繼承自 BaseDialogNode)
const BeginModuleFlowNode = BaseDialogNode.extend({
  Type: z.literal("flow.module.begin").describe("Node 類型：flow.module.begin"),
  Message: MessageContent.optional().describe("訊息內容（二擇一）"),
  Messages: z.array(MessageContent).optional().describe("多個訊息內容（二擇一）"),
  FlowId: z.string().describe("呼叫的 Module Flow ID"),
  Arguments: z.record(FlowControlArgument).describe("指派呼叫的 Module Flow 的流程變數")
});

// Switch Flow Node Schema (基於 SwitchFlow.md，繼承自 BaseDialogNode)
const SwitchFlowNode = BaseDialogNode.extend({
  Type: z.literal("flow.switch").describe("Node 類型：flow.switch"),
  Message: MessageContent.optional().describe("訊息內容（二擇一）"),
  Messages: z.array(MessageContent).optional().describe("多個訊息內容（二擇一）"),
  FlowId: z.string().describe("呼叫的 Flow ID"),
  Arguments: z.record(FlowControlArgument).describe("指派呼叫的 Flow 的流程變數")
});

// Flow Return Value Schema (基於 EndCurrentFlow.md 和 EndModuleFlow.md)
const FlowReturnValue = z.object({
  Type: z.enum([
    "string", 
    "string.json", 
    "number", 
    "boolean", 
    "object", 
    "array", 
    "variable", 
    "evaluate_expression"
  ]).describe("輸出資料的取值類型"),
  Value: z.any().describe("回傳值")
});

// End All Flow Node Schema (基於 EndAllFlow.md，繼承自 BaseDialogNode)
const EndAllFlowNode = BaseDialogNode.extend({
  Type: z.literal("flow.end.all").describe("Node 類型：flow.end.all"),
  Message: MessageContent.optional().describe("訊息內容（二擇一）"),
  Messages: z.array(MessageContent).optional().describe("多個訊息內容（二擇一）")
});

// End Current Flow Node Schema (基於 EndCurrentFlow.md，繼承自 BaseDialogNode)
const EndCurrentFlowNode = BaseDialogNode.extend({
  Type: z.literal("flow.end.current").describe("Node 類型：flow.end.current"),
  Message: MessageContent.optional().describe("訊息內容（二擇一）"),
  Messages: z.array(MessageContent).optional().describe("多個訊息內容（二擇一）"),
  ReturnValue: FlowReturnValue.optional().describe("流程輸出資料（回傳值）")
});

// End Module Flow Node Schema (基於 EndModuleFlow.md，繼承自 BaseDialogNode)
const EndModuleFlowNode = BaseDialogNode.extend({
  Type: z.literal("flow.module.end").describe("Node 類型：flow.module.end"),
  Message: MessageContent.optional().describe("訊息內容（二擇一）"),
  Messages: z.array(MessageContent).optional().describe("多個訊息內容（二擇一）"),
  ReturnValue: FlowReturnValue.optional().describe("模組流程輸出資料（回傳值）")
});

// ==========================================
// External Node Schemas (基於 Nodes/External/*.md)
// ==========================================

// Response Options Schema (基於 BaseRequest.md)
const ResponseOptions = z.object({
  Headers: z.string().default("").describe("拿取的 Http Response Header Name，預設值：空字串。可以是：空字串（不拿取）、'Header1,Header2'（指定Header）、'*'（全部Header）")
});

// Auto Upload Binary Options Schema (基於 RequestRawDataOrBinary.md)
const AutoUploadBinaryOptions = z.object({
  IsEnable: z.boolean().default(false).describe("如果為 true 代表啟用此功能，預設值：false"),
  ExpirationTime: z.string().default("1.00:00:00").describe("設定檔案多久過期，格式 [dd.]hh:mm:ss，預設值：1.00:00:00（一天）")
});

// Base Request Node Schema (基於 BaseRequest.md，繼承自 BaseDialogNode)
const BaseRequestNode = BaseDialogNode.extend({
  Method: z.enum(["GET", "POST", "PUT", "PATCH", "DELETE"]).describe("HTTP 方法"),
  Url: z.string().describe("URL"),
  Headers: z.record(z.string()).optional().describe("Headers"),
  Body: z.any().optional().describe("Body"),
  Timeout: z.number().int().default(100).describe("Timeout 時間，預設值：100（秒）"),
  ResponseOptions: ResponseOptions.optional().describe("Http Response 解析設定")
});

// Request Raw Data Node Schema (基於 RequestRawData.md，繼承自 BaseRequest)
const RequestRawDataNode = BaseRequestNode.extend({
  Type: z.literal("request.raw").describe("Node 類型：request.raw"),
  ContentType: z.string().default("text").describe("Content Type，預設值：text")
});

// Request Raw JSON Node Schema (基於 RequestRawJson.md，繼承自 BaseRequest)
const RequestRawJsonNode = BaseRequestNode.extend({
  Type: z.literal("request.json").describe("Node 類型：request.json")
});

// Request Form Data Node Schema (基於 RequestFormData.md，繼承自 BaseRequest)
const RequestFormDataNode = BaseRequestNode.extend({
  Type: z.literal("request.form").describe("Node 類型：request.form"),
  ContentType: z.enum(["multipart", "form"]).default("multipart").describe("Content Type，預設值：multipart"),
  Body: z.record(z.string()).optional().describe("Body (Form Data)")
});

// Request Raw Data Or Binary Node Schema (基於 RequestRawDataOrBinary.md，繼承自 BaseRequest)
const RequestRawDataOrBinaryNode = BaseRequestNode.extend({
  Type: z.literal("request.binary").describe("Node 類型：request.binary"),
  ContentType: z.string().default("text").describe("Content Type，預設值：text"),
  AutoUploadBinaryOptions: AutoUploadBinaryOptions.optional().describe("自動將 Http Response Binary 檔案上傳到 File Server 的參數設定")
});

// Http Request Schema for Parallel and Multicast Request (基於 ParallelRequest.md 和 MulticastRequest.md)
const HttpRequest = z.object({
  Method: z.enum(["GET", "POST", "PUT", "PATCH", "DELETE"]).describe("HTTP 方法"),
  Url: z.string().describe("URL"),
  ContentType: z.string().describe("Content Type"),
  Headers: z.record(z.string()).optional().describe("Headers"),
  RawBody: z.any().optional().describe("Raw Body（僅限非 Form Data 類型）"),
  FormBody: z.record(z.string()).optional().describe("Form Body（僅限 Form 或 Form Data 類型）"),
  Timeout: z.number().int().default(100).describe("Timeout 時間，預設值：100（秒）"),
  ResponseOptions: ResponseOptions.optional().describe("Http Response 解析設定")
});

// Parallel Request Node Schema (基於 ParallelRequest.md，繼承自 BaseDialogNode)
const ParallelRequestNode = BaseDialogNode.extend({
  Type: z.literal("request.parallel").describe("Node 類型：request.parallel"),
  Mode: z.enum(["parallel", "sequence"]).default("parallel").describe("執行的模式，預設值：parallel"),
  Requests: z.array(HttpRequest.extend({
    Id: z.string().describe("Request ID，同一個 Node 不得重複")
  })).describe("多個 Http Request，陣列中 Request.Id 不得重複")
});

// Multicast Request Node Schema (基於 MulticastRequest.md，繼承自 BaseDialogNode)
const MulticastRequestNode = BaseDialogNode.extend({
  Type: z.literal("request.multicast").describe("Node 類型：request.multicast"),
  Mode: z.enum(["parallel", "sequence"]).default("parallel").describe("執行的模式，預設值：parallel"),
  Request: HttpRequest.describe("Http Request"),
  RequestIdPrefix: z.string().default("data").describe("指定 Http Request Id Prefix，預設值：data"),
  DataSource: z.string().describe("指定資料來源（變數），變數的資料型態需為一個陣列")
});

// ==========================================
// Prompt Node Schemas (基於 Nodes/Prompt/*.md)
// ==========================================

// Prompt Validator Schema (基於 BasePrompt.md#prompt-validator)
const PromptValidator = z.object({
  Rules: z.array(BaseRule).describe("文字條件"),
  Type: z.enum(["and", "or", "none"]).default("and").describe("多組條件的判斷，預設值為 and")
});

// Base Prompt Schema (基於 BasePrompt.md)
const BasePrompt = BaseDialogNode.extend({
  Prompt: MessageContent.describe("提示使用者需要的內容，例如：文字、卡片"),
  Retry: MessageContent.optional().describe("提示使用者輸入錯誤，未設定時沿用 Prompt 的設定"),
  RetryMaxCount: z.number().int().default(-1).describe("重新輸入最大次數，預設為 -1 (沒有限制次數)"),
  Validator: PromptValidator.optional().describe("驗證使用者輸入的格式")
});

// Prompt Text Node Schema (基於 PromptText.md，繼承自 BasePrompt)
const PromptTextNode = BasePrompt.extend({
  Type: z.literal("prompt.text").describe("Node 類型：prompt.text")
});

// Prompt Card Node Schema (基於 PromptCard.md，繼承自 BasePrompt)
const PromptCardNode = BasePrompt.extend({
  Type: z.literal("prompt.card").describe("Node 類型：prompt.card")
});

// Prompt Adaptive Card Node Schema (基於 PromptAdaptiveCard.md，繼承自 BasePrompt)
const PromptAdaptiveCardNode = BasePrompt.extend({
  Type: z.literal("prompt.adaptivecard").describe("Node 類型：prompt.adaptivecard")
});

// ==========================================
// QA Node Schemas (基於 Nodes/QA/*.md)
// ==========================================

// Base QA Schema (基於 BaseQA.md，繼承自 BaseDialogNode)
const BaseQA = BaseDialogNode.extend({
  Prompt: MessageContent.optional().describe("提示使用者輸入問題"),
  IsPrompt: z.boolean().describe("是否提示或等候使用者輸入")
});

// Regex Model Schema (基於 QARegex.md#regexmodel)
const RegexModel = z.object({
  Intent: z.string().describe("意圖"),
  Patterns: z.array(z.string()).describe("符合此意圖句型"),
  IgnoreCase: z.boolean().default(true).optional().describe("忽略大小寫，預設值 true")
});

// QA Regex Node Schema (基於 QARegex.md，繼承自 BaseQA)
const QARegexNode = BaseQA.extend({
  Type: z.literal("qa.regex").describe("Node 類型：qa.regex"),
  Models: z.array(RegexModel).describe("Regex Model")
});

// QA LUIS Node Schema (基於 QALuis.md，繼承自 BaseQA)
const QALuisNode = BaseQA.extend({
  Type: z.literal("qa.luis").describe("Node 類型：qa.luis"),
  Region: z.string().describe("Azure LUIS 地區 (服務的主機)，預設 Free Key為 westus"),
  ApplicationId: z.string().describe("LUIS Application Id"),
  SubscriptionKey: z.string().describe("LUIS Subscription Key")
});

// QA GSS AI Node Schema (基於 QAGssAI.md，繼承自 BaseQA)
const QAGssAINode = BaseQA.extend({
  Type: z.literal("qa.gssai").describe("Node 類型：qa.gssai"),
  HostUrl: z.string().describe("GSS.AI 的 Host URL"),
  ApplicationId: z.string().describe("GSS.AI 對應的 App Id"),
  SubscriptionKey: z.string().describe("GSS.AI Subscription Key"),
  AnswerCount: z.string().describe("答案數量"),
  Confidence: z.string().describe("答案的信心指數")
});

// Quit Action Schema (基於 QAGssQA.md#quit-action)
const QuitAction = z.object({
  Title: z.string().describe("標題"),
  Value: z.string().describe("指定關鍵字，其值必須符合 Pattern 規則"),
  Pattern: z.string().default("^(quit)$").describe("符合的格式，不分大小寫，以 Regular Expression 表示，預設：^(quit)$")
});

// Feedback Action Schema (基於 QAGssQA.md#feedback-action)
const FeedbackAction = z.object({
  IsEnabled: z.boolean().default(false).describe("是否啟用問答回饋，預設值：false"),
  ActionTitle: z.string().describe("問答回饋按鈕標題"),
  ActionReply: z.string().describe("使用者點擊問答回饋後，Bot 回覆的訊息")
});

// QA GSS QA Node Schema (基於 QAGssQA.md，繼承自 BaseQA)
const QAGssQANode = BaseQA.extend({
  Type: z.literal("qa.gssqa").describe("Node 類型：qa.gssqa"),
  Retry: MessageContent.optional().describe("提示使用者找不到答案，提示換一個問法。如果沒有設定會使用系統預設訊息"),
  NoMatchMessage: z.string().describe("找不到問題的訊息"),
  ApplicationId: z.string().describe("GSS 對話管理平台的 App ID"),
  SubscriptionKey: z.string().describe("GSS.AI Subscription Key"),
  AnswerCount: z.string().describe("顯示的答案數量，預設 3筆 (限定 Intent 為 FAQ)"),
  Confidence: z.string().describe("答案的信心指數最低標準，預設 0.7 (限定 Intent 為 FAQ)"),
  Role: z.string().optional().describe("角色身分"),
  FlowBeginMode: z.string().default("default").describe("切換其他 flow 的方式，預設：default"),
  QuitAction: QuitAction.optional().describe("跳脫提問的對話相關設定，不設定此 Property 則不顯示相關提示按鈕"),
  FeedbackAction: FeedbackAction.optional().describe("問答回饋按鈕")
});

// ==========================================
// Send Node Schemas (基於 Nodes/Send/*.md)
// ==========================================

// Event Content Schema (基於 Contents/EventContent.md)
const EventContent = z.object({
  Type: z.literal("event").describe("類型，值為 event"),
  MessageType: z.enum(["event", "invoke", "typing", "trace"]).default("typing").describe("訊息類型"),
  Name: z.string().describe("名稱"),
  DataType: z.enum(["string", "object"]).describe("資料的型態"),
  Data: z.string().describe("資料"),
  QuickReply: z.array(z.any()).optional().describe("快速回覆按鈕"),
  ChannelDataPayload: z.any().optional().describe("Channel Data Payload")
});

// Send Message Node Schema (基於 SendMessage.md，繼承自 BaseDialogNode)
const SendMessageNode = BaseDialogNode.extend({
  Type: z.literal("send.message").describe("Node 類型：send.message"),
  Message: MessageContent.describe("訊息內容（二擇一）"),
  Messages: z.array(MessageContent).describe("多個訊息內容（二擇一）")
});

// Send Event Node Schema (基於 SendEvent.md，繼承自 BaseDialogNode)
const SendEventNode = BaseDialogNode.extend({
  Type: z.literal("send.event").describe("Node 類型：send.event"),
  EventName: EventContent.describe("事件訊息內容")
});

// Send Carousel Node Schema (基於 SendCarousel.md，繼承自 BaseDialogNode)
const SendCarouselNode = BaseDialogNode.extend({
  Type: z.literal("send.carousel").describe("Node 類型：send.carousel"),
  Text: z.string().optional().describe("卡片訊息內容"),
  Attachments: z.array(MessageContent).describe("發送使用者需要的卡片，只支援部分訊息類型"),
  AttachmentLayout: z.enum(["list", "carousel"]).default("carousel").describe("卡片的排版，預設值: carousel")
});

// Typing Message Node Schema (基於 TypingMessage.md，繼承自 BaseDialogNode)
const TypingMessageNode = BaseDialogNode.extend({
  Type: z.literal("typing.message").describe("Node 類型：typing.message"),
  Text: z.string().describe("文字訊息"),
  TypingInterval: z.number().int().default(500).optional().describe("打字的間隔時間，預設值：500 (500毫秒)"),
  DisableTyping: z.boolean().default(false).optional().describe("是否停止打字效果，預設值：false")
});

// Base Trace Node Schema (基於 Trace/BaseTrace.md，繼承自 BaseDialogNode)
const BaseTraceNode = BaseDialogNode.extend({
  // 基礎 BaseDialogNode 屬性已包含在內
});

// Trace Node Schema (基於 Trace/Trace.md，繼承自 BaseTraceNode)
const TraceNode = BaseTraceNode.extend({
  Type: z.literal("trace").describe("Node 類型：trace"),
  Messages: z.array(MessageContent).optional().describe("顯示訊息"),
  TraceName: z.string().describe("Trace 名稱"),
  TraceLabel: z.string().optional().describe("Trace 標籤"),
  TraceValueType: z.string().optional().describe("Trace 資料的資料類型"),
  TraceValue: z.any().describe("Trace 資料")
});

// Variable Decision Node Schema (基於 VariableControl/VariableDecision.md，繼承自 BaseDialogNode)
const VariableDecisionNode = BaseDialogNode.extend({
  Type: z.literal("variable").describe("Node 類型：variable"),
  VariableActions: z.array(VariableAction).describe("Variable 相關操作，按照 Array 順序處理")
});


// ==========================================
// Event Schemas (基於 Events/*.md)
// ==========================================

// Flow Condition Schema (基於 BaseEvent.md#flow-condition)
const FlowCondition = z.object({
  Type: z.enum(["none", "flow", "flow.empty", "flow.excluded", "node", "node.excluded"]).default("none").describe("檢查類型，預設值：none (不限定對話流程、節點)"),
  Value: z.string().describe("在指定對話流程、節點啟用，多個對話流程/節點時以 , 間隔")
});

// Event Action Argument Schema (基於 EventAction.md#argument)
const EventActionArgument = z.object({
  $Type: z.enum(["use_expression", "plain", "variable"]).default("use_expression").describe("引數的類型，預設值：use_expression"),
  $Value: z.any().describe("引數的值")
});

// Base Event Action Schema (基於 EventAction.md)
const BaseEventAction = z.object({
  Type: z.enum(["message", "flow", "flow.module", "composite"]).describe("觸發行為類型")
});

// Message Event Action Schema (基於 EventAction.md#message-event-action)
const MessageEventAction = BaseEventAction.extend({
  Type: z.literal("message").describe("觸發行為類型，值為 message"),
  Messages: z.array(MessageContent).describe("訊息"),
  VariableActions: z.array(VariableAction).optional().describe("變數操作")
});

// Flow Event Action Schema (基於 EventAction.md#flow-event-action)
const FlowEventAction = BaseEventAction.extend({
  Type: z.literal("flow").describe("觸發行為類型，值為 flow"),
  FlowId: z.string().describe("流程 ID"),
  Arguments: z.record(EventActionArgument).optional().describe("指派呼叫的 Flow 的流程變數"),
  VariableActions: z.array(VariableAction).describe("變數操作")
});

// Module Flow Event Action Schema (基於 EventAction.md#module-event-action)
const ModuleFlowEventAction = BaseEventAction.extend({
  Type: z.literal("flow.module").describe("觸發行為類型，值為 flow.module"),
  FlowId: z.string().describe("流程 ID"),
  Arguments: z.record(EventActionArgument).optional().describe("指派呼叫的 Flow 的流程變數"),
  VariableActions: z.array(VariableAction).describe("變數操作")
});

// Composite Event Action Condition Schema (基於 EventAction.md#composite-event-action-conditions)
const CompositeEventActionCondition = z.object({
  Name: z.string().describe("Action 的名稱或敘述"),
  Rules: z.array(BaseRule).describe("條件"),
  Type: z.enum(["and", "or"]).default("or").describe("條件符合的方式，預設值為 or"),
  Priority: z.number().min(0).max(100).describe("Action的優先順序，範圍 0 ~ 100"),
  Action: z.lazy(() => EventAction).describe("當條件符合時，的處理動作")
});

// Composite Event Action Schema (基於 EventAction.md#composite-event-action)
const CompositeEventAction = BaseEventAction.extend({
  Type: z.literal("composite").describe("觸發行為類型，值為 composite"),
  Conditions: z.array(CompositeEventActionCondition).describe("Event Action 邏輯判斷"),
  VariableActions: z.array(VariableAction).describe("變數操作")
});

// Event Action Union Schema
const EventAction = z.union([
  MessageEventAction,
  FlowEventAction,
  ModuleFlowEventAction,
  CompositeEventAction
]).describe("事件動作（所有事件動作類型的聯集）");

// Event Action Condition Schema (通用的事件動作條件)
const EventActionCondition = z.object({
  Rules: z.array(BaseRule).describe("條件"),
  Type: z.enum(["and", "or"]).default("and").describe("多組條件的判斷，預設值為 and")
});

// Base Event Schema (基於 BaseEvent.md)
const BaseEvent = z.object({
  Id: z.string().describe("ID"),
  Description: z.string().optional().describe("敘述"),
  Type: z.enum(["greeting", "message", "notification", "event", "conversation.timeout"]).describe("Event 類型"),
  Action: EventAction.describe("當事件成立時的動作"),
  Priority: z.number().min(0).max(100).default(50).describe("Hook 事件的優先順序，範圍 0 ~ 100，預設值：50"),
  FlowConditions: z.array(FlowCondition).optional().describe("在指定對話流程 ID或對話節點 ID中使用，預設值：空陣列 (不限定對話流程或節點)"),
  IsEnable: z.boolean().describe("是否啟用，true: 啟用、false: 停用")
});

// Greeting Event Schema (基於 GreetingEvent.md)
const GreetingEvent = BaseEvent.extend({
  Type: z.literal("greeting").describe("Event 類型，值為 greeting"),
  IsEnabledAtFirst: z.boolean().default(false).optional().describe("是否只在對話的一次觸發時執行，預設值：false (允許多次觸發)"),
  ActionConditions: EventActionCondition.optional().describe("迎賓事件的自訂觸發條件，會在動作 (包含變數操作) 之前判斷，預設值：為空 (沒有條件限制)")
});

// Message Condition Schema (基於 UserMessageEvent.md#message-condition)
const MessageCondition = z.object({
  Rules: z.array(BaseRule).describe("觸發條件規則"),
  Type: z.enum(["and", "or"]).default("and").describe("多組條件的判斷，預設值為 and")
});

// User Message Event Schema (基於 UserMessageEvent.md)
const UserMessageEvent = BaseEvent.extend({
  Type: z.literal("message").describe("Event 類型，值為 message"),
  MessageConditions: MessageCondition.describe("觸發條件規則，在這裡會依據條件規則去判斷是否處理這個訊息")
});

// Notification Event Schema (基於 NotificationEvent.md)
const NotificationEvent = BaseEvent.extend({
  Type: z.literal("notification").describe("Event 類型，值為 notification"),
  NotificationName: z.string().describe("符合的通知名稱，在這裡會依據 Notification Name 去判斷是否觸發這個訊息"),
  ActionConditions: EventActionCondition.optional().describe("通知事件之自訂觸發條件，會在動作 (包含變數操作) 之前判斷，預設值：為空 (沒有條件限制)")
});

// Custom Event Schema (基於 CustomEvent.md)
const CustomEvent = BaseEvent.extend({
  Type: z.literal("event").describe("Event 類型，值為 event"),
  EventName: z.string().describe("符合的Event 名稱，在這裡會依據 Event Name去判斷是否處理這個訊息"),
  ActionConditions: EventActionCondition.optional().describe("自訂事件之自訂觸發條件，會在動作 (包含變數操作) 之前判斷，預設值：為空 (沒有條件限制)")
});

// Conversation Timeout Event Schema (基於 ConversationTimeoutEvent.md)
const ConversationTimeoutEvent = BaseEvent.extend({
  Type: z.literal("conversation.timeout").describe("Event 類型，值為 conversation.timeout"),
  Timeout: z.number().default(0).describe("逾時時間，單位以分鐘計算，預設值：0 (無 timeout)")
});

// Event Union Schema (所有事件類型的聯集)
const Event = z.union([
  GreetingEvent,
  UserMessageEvent,
  NotificationEvent,
  CustomEvent,
  ConversationTimeoutEvent
]).describe("事件（所有事件類型的聯集）");

// ==========================================
// Dialog Flow Schema (基於 Flows/DialogFlow.md)
// ==========================================
const DialogFlow = z.object({
  Id: z.string().describe("Dialog Flow ID (唯一)"),
  Name: z.string().optional().describe("Dialog Flow 名稱"),
  Description: z.string().optional().describe("Dialog Flow 描述"),
  IsModuleFlow: z.boolean().default(false).describe("Dialog Flow 是否為一個模組流程"),
  StartNodeId: z.string().describe("開始的 Node ID"),
  Nodes: z.array(BaseDialogNode).describe("Dialog Node 陣列")
});

// ==========================================
// Variable Schemas (基於 Variables/Variable.md)
// ==========================================
// 使用者訊息變數
const MessageVariable = z.object({
  Text: z.string().optional().describe("使用者發送的訊息"),
  Value: z.any().optional().describe("使用者發送的卡片資料訊息"),
  Attachments: z.array(z.any()).optional().describe("使用者發送的附件訊息"),
  Id: z.string().optional().describe("訊息編號"),
  TimeStamp: z.string().optional().describe("收到的訊息時間")
});

// 對話資訊變數
const ConversationVariable = z.object({
  UserId: z.string().describe("使用者ID"),
  UserName: z.string().optional().describe("使用者名稱"),
  BotId: z.string().describe("Bot ID"),
  ChannelId: z.string().describe("Channel ID"),
  IsGroup: z.boolean().describe("是否為群組"),
  Id: z.string().describe("Conversation ID"),
  ChannelData: z.any().optional().describe("Channel Data")
});

// 節點輸出值變數
const NodeOutputVariable = z.object({
  Data: z.any().describe("資料值"),
  Type: z.string().describe("資料型態"),
  From: z.object({
    FlowId: z.string().describe("輸出的流程 ID"),
    NodeId: z.string().describe("輸出的節點 ID"),
    NodeName: z.string().describe("輸出的節點名稱"),
    NodeType: z.string().describe("輸出的節點類型")
  }).optional().describe("輸出來源資訊")
});

// 對話流程與節點資訊變數
const DialogStateVariable = z.object({
  FlowId: z.string().describe("目前的對話流程 ID"),
  FlowName: z.string().describe("目前的對話流程名稱"),
  NodeId: z.string().describe("目前的對話節點 ID"),
  NodeName: z.string().describe("目前的對話節點名稱"),
  NodeType: z.string().describe("目前的對話節點類型")
});

// 事件變數
const EventVariable = z.object({
  ChannelId: z.string().describe("Channel ID"),
  UserId: z.string().describe("User ID"),
  UserName: z.string().describe("User Name"),
  BotId: z.string().describe("Bot ID"),
  IsGroup: z.boolean().describe("Is Group"),
  ChannelData: z.any().optional().describe("Channel Data"),
  // 使用者訊息事件專用
  Text: z.string().optional().describe("文字訊息"),
  Value: z.any().optional().describe("資料"),
  Attachments: z.array(z.any()).optional().describe("卡片"),
  // 迎賓事件專用
  JoinMembers: z.array(z.object({
    Id: z.string().describe("使用者ID"),
    Name: z.string().describe("使用者名稱")
  })).optional().describe("加入的使用者陣列"),
  EventHitCount: z.number().optional().describe("迎賓事件觸發的次數"),
  LastUpdateDate: z.string().optional().describe("前一次迎賓事件觸發的時間"),
  // 通知/自訂事件專用
  EventName: z.string().optional().describe("Event 名稱"),
  EventLabel: z.string().optional().describe("Event Label"),
  EventValueType: z.string().optional().describe("Event Value 的資料類型"),
  EventValue: z.any().optional().describe("Event Value")
});

// 完整的變數上下文
const VariableContext = z.object({
  Message: MessageVariable.optional().describe("使用者訊息"),
  Conversation: ConversationVariable.describe("對話資訊"),
  NodeOutput: NodeOutputVariable.optional().describe("節點輸出值"),
  DialogState: DialogStateVariable.optional().describe("對話流程與節點資訊"),
  EventVariables: EventVariable.optional().describe("事件變數"),
  Configs: z.record(z.any()).optional().describe("預設組態"),
  Variables: z.record(z.any()).optional().describe("全域自訂變數"),
  FlowVariables: z.record(z.any()).optional().describe("流程自訂變數"),
  NodeVariables: z.record(z.any()).optional().describe("節點自訂變數")
});

// ==========================================
// Expression Schemas (基於 Expression.md)
// ==========================================
const ExpressionEvaluation = z.object({
  type: z.enum([
    "jsonpath",
    "csharp", 
    "javascript",
    "adaptive"
  ]).describe("表達式類型"),
  expression: z.string().describe("表達式內容"),
  result: z.any().describe("評估結果"),
  error: z.string().optional().describe("評估錯誤訊息")
});

// ==========================================
// Bot Configuration Schema (基於 Bot.md)
// ==========================================
const BotSettings = z.object({
  Name: z.string().describe("Bot Setting 名稱"),
  Plugins: z.array(z.object({
    Id: z.string().describe("Plugin ID"),
    IsEnabled: z.boolean().describe("是否啟用")
  })).optional().describe("Bot Plugin 設定"),
  MaxNodeAccessCountPerTurn: z.number().optional().describe("每個節點最大訪問次數"),
  CertificateValidation: z.boolean().optional().describe("是否啟用憑證檢查")
});

const BotConfiguration = z.object({
  Id: z.string().describe("Bot 的 ID (唯一)"),
  Version: z.string().describe("Bot Script 版本"),
  SchemaVersion: z.string().optional().describe("Bot Schema 版本"),
  Profile: z.record(z.any()).optional().describe("Bot Profile"),
  Configs: z.record(z.any()).optional().describe("Bot 預設變數 (唯讀)"),
  BotSettings: z.array(BotSettings).optional().describe("Bot 內部系統設定"),
  StartFlowId: z.string().describe("入口的流程 ID"),
  Flows: z.array(DialogFlow).describe("所有流程"),
  Events: z.array(z.any()).optional().describe("全域事件處理")
});

// ==========================================
// Conversational AI Response Schemas
// ==========================================

// 對話決策結果
const ConversationDecision = z.object({
  should_continue: z.boolean().describe("是否應該繼續對話"),
  next_flow_id: z.string().optional().describe("下一個流程ID"),
  next_node_id: z.string().optional().describe("下一個節點ID"),
  response_type: z.enum([
    "message",
    "prompt", 
    "end_conversation",
    "switch_flow",
    "call_api"
  ]).describe("回應類型"),
  confidence: z.number().min(0).max(1).optional().describe("決策信心度")
});

// 自然語言理解結果
const NLUResult = z.object({
  intent: z.string().describe("識別的意圖"),
  confidence: z.number().min(0).max(1).describe("信心度"),
  entities: z.array(z.object({
    type: z.string().describe("實體類型"),
    value: z.string().describe("實體值"),
    start: z.number().describe("起始位置"),
    end: z.number().describe("結束位置")
  })).optional().describe("識別的實體"),
  matched_rule: z.string().optional().describe("匹配的規則")
});

// 對話流程執行結果
const FlowExecutionResult = z.object({
  success: z.boolean().describe("執行是否成功"),
  current_flow_id: z.string().describe("目前流程ID"),
  current_node_id: z.string().describe("目前節點ID"),
  variables_updated: z.record(z.any()).optional().describe("更新的變數"),
  output_message: z.string().optional().describe("輸出訊息"),
  next_action: ConversationDecision.optional().describe("下一個行動"),
  error_message: z.string().optional().describe("錯誤訊息")
});

// 變數操作結果
const VariableOperationResult = z.object({
  operation: z.enum(["set", "get", "remove", "evaluate"]).describe("操作類型"),
  variable_name: z.string().describe("變數名稱"),
  variable_type: z.enum(["global", "flow", "node"]).describe("變數類型"),
  old_value: z.any().optional().describe("舊值"),
  new_value: z.any().optional().describe("新值"),
  success: z.boolean().describe("操作是否成功"),
  error_message: z.string().optional().describe("錯誤訊息")
});


// ==========================================
// Export schemas for OpenAI structured outputs
// ==========================================
export const openaiSchemas = {
  // 核心結構
  nodeAction: zodResponseFormat(NodeAction, "node_action"),
  variableAction: zodResponseFormat(VariableAction, "variable_action"),
  baseDialogNode: zodResponseFormat(BaseDialogNode, "base_dialog_node"),
  dialogFlow: zodResponseFormat(DialogFlow, "dialog_flow"),
  botConfiguration: zodResponseFormat(BotConfiguration, "bot_configuration"),
  
  // AI 相關
  aiChatMessage: zodResponseFormat(AIChatMessage, "ai_chat_message"),
  baseAIChatNode: zodResponseFormat(BaseAIChatNode, "base_ai_chat_node"),
  aoaiChatEndpoint: zodResponseFormat(AOAIChatEndpoint, "aoai_chat_endpoint"),
  aoaiChatOptions: zodResponseFormat(AOAIChatOptions, "aoai_chat_options"),
  azureOpenAIChatNode: zodResponseFormat(AzureOpenAIChatNode, "azure_openai_chat_node"),
  
  // Custom 相關
  customDialogParameter: zodResponseFormat(CustomDialogParameter, "custom_dialog_parameter"),
  customDialogNode: zodResponseFormat(CustomDialogNode, "custom_dialog_node"),
  customFunctionArgument: zodResponseFormat(CustomFunctionArgument, "custom_function_argument"),
  javaScriptLibrary: zodResponseFormat(JavaScriptLibrary, "javascript_library"),
  customFunctionNode: zodResponseFormat(CustomFunctionNode, "custom_function_node"),
  
  // Prompt 相關
  promptValidator: zodResponseFormat(PromptValidator, "prompt_validator"),
  basePrompt: zodResponseFormat(BasePrompt, "base_prompt"),
  promptTextNode: zodResponseFormat(PromptTextNode, "prompt_text_node"),
  promptCardNode: zodResponseFormat(PromptCardNode, "prompt_card_node"),
  promptAdaptiveCardNode: zodResponseFormat(PromptAdaptiveCardNode, "prompt_adaptive_card_node"),
  
  // QA 相關
  baseQA: zodResponseFormat(BaseQA, "base_qa"),
  regexModel: zodResponseFormat(RegexModel, "regex_model"),
  qaRegexNode: zodResponseFormat(QARegexNode, "qa_regex_node"),
  qaLuisNode: zodResponseFormat(QALuisNode, "qa_luis_node"),
  qaGssAINode: zodResponseFormat(QAGssAINode, "qa_gss_ai_node"),
  quitAction: zodResponseFormat(QuitAction, "quit_action"),
  feedbackAction: zodResponseFormat(FeedbackAction, "feedback_action"),
  qaGssQANode: zodResponseFormat(QAGssQANode, "qa_gss_qa_node"),
  
  // Send 相關
  sendMessageNode: zodResponseFormat(SendMessageNode, "send_message_node"),
  sendEventNode: zodResponseFormat(SendEventNode, "send_event_node"),
  sendCarouselNode: zodResponseFormat(SendCarouselNode, "send_carousel_node"),
  typingMessageNode: zodResponseFormat(TypingMessageNode, "typing_message_node"),
  
  // Trace 相關
  baseTraceNode: zodResponseFormat(BaseTraceNode, "base_trace_node"),
  traceNode: zodResponseFormat(TraceNode, "trace_node"),
  
  // Variable Control 相關
  variableDecisionNode: zodResponseFormat(VariableDecisionNode, "variable_decision_node"),
  
  // Events 相關
  flowCondition: zodResponseFormat(FlowCondition, "flow_condition"),
  eventActionArgument: zodResponseFormat(EventActionArgument, "event_action_argument"),
  baseEventAction: zodResponseFormat(BaseEventAction, "base_event_action"),
  messageEventAction: zodResponseFormat(MessageEventAction, "message_event_action"),
  flowEventAction: zodResponseFormat(FlowEventAction, "flow_event_action"),
  moduleFlowEventAction: zodResponseFormat(ModuleFlowEventAction, "module_flow_event_action"),
  compositeEventActionCondition: zodResponseFormat(CompositeEventActionCondition, "composite_event_action_condition"),
  compositeEventAction: zodResponseFormat(CompositeEventAction, "composite_event_action"),
  eventAction: zodResponseFormat(EventAction, "event_action"),
  eventActionCondition: zodResponseFormat(EventActionCondition, "event_action_condition"),
  baseEvent: zodResponseFormat(BaseEvent, "base_event"),
  greetingEvent: zodResponseFormat(GreetingEvent, "greeting_event"),
  messageCondition: zodResponseFormat(MessageCondition, "message_condition"),
  userMessageEvent: zodResponseFormat(UserMessageEvent, "user_message_event"),
  notificationEvent: zodResponseFormat(NotificationEvent, "notification_event"),
  customEvent: zodResponseFormat(CustomEvent, "custom_event"),
  conversationTimeoutEvent: zodResponseFormat(ConversationTimeoutEvent, "conversation_timeout_event"),
  event: zodResponseFormat(Event, "event"),
  
  // Flow Control 相關
  flowControlArgument: zodResponseFormat(FlowControlArgument, "flow_control_argument"),
  messageContent: zodResponseFormat(MessageContent, "message_content"),
  eventContent: zodResponseFormat(EventContent, "event_content"),
  beginFlowNode: zodResponseFormat(BeginFlowNode, "begin_flow_node"),
  beginModuleFlowNode: zodResponseFormat(BeginModuleFlowNode, "begin_module_flow_node"),
  switchFlowNode: zodResponseFormat(SwitchFlowNode, "switch_flow_node"),
  flowReturnValue: zodResponseFormat(FlowReturnValue, "flow_return_value"),
  endAllFlowNode: zodResponseFormat(EndAllFlowNode, "end_all_flow_node"),
  endCurrentFlowNode: zodResponseFormat(EndCurrentFlowNode, "end_current_flow_node"),
  endModuleFlowNode: zodResponseFormat(EndModuleFlowNode, "end_module_flow_node"),
  
  // External 相關
  responseOptions: zodResponseFormat(ResponseOptions, "response_options"),
  autoUploadBinaryOptions: zodResponseFormat(AutoUploadBinaryOptions, "auto_upload_binary_options"),
  baseRequestNode: zodResponseFormat(BaseRequestNode, "base_request_node"),
  requestRawDataNode: zodResponseFormat(RequestRawDataNode, "request_raw_data_node"),
  requestRawJsonNode: zodResponseFormat(RequestRawJsonNode, "request_raw_json_node"),
  requestFormDataNode: zodResponseFormat(RequestFormDataNode, "request_form_data_node"),
  requestRawDataOrBinaryNode: zodResponseFormat(RequestRawDataOrBinaryNode, "request_raw_data_or_binary_node"),
  httpRequest: zodResponseFormat(HttpRequest, "http_request"),
  parallelRequestNode: zodResponseFormat(ParallelRequestNode, "parallel_request_node"),
  multicastRequestNode: zodResponseFormat(MulticastRequestNode, "multicast_request_node"),
  
  // 變數相關
  variableContext: zodResponseFormat(VariableContext, "variable_context"),
  variableOperationResult: zodResponseFormat(VariableOperationResult, "variable_operation_result"),
  
  // 表達式相關
  expressionEvaluation: zodResponseFormat(ExpressionEvaluation, "expression_evaluation"),
  
  // 對話流程相關
  conversationDecision: zodResponseFormat(ConversationDecision, "conversation_decision"),
  nluResult: zodResponseFormat(NLUResult, "nlu_result"),
  flowExecutionResult: zodResponseFormat(FlowExecutionResult, "flow_execution_result")
};

// ==========================================
// Usage Examples
// ==========================================

/*
// 1. Node Action 創建範例
const nodeActionResponse = await openai.chat.completions.create({
  model: "gpt-4o-2024-08-06",
  messages: [
    {
      role: "system",
      content: "你是一個對話流程設計助手，請根據使用者需求創建 Node Action"
    },
    {
      role: "user",
      content: "創建一個 Node Action，當使用者輸入 'help' 時轉換到幫助節點"
    }
  ],
  response_format: openaiSchemas.nodeAction
});

// 2. 變數操作範例
const variableOpResponse = await openai.chat.completions.create({
  model: "gpt-4o-2024-08-06",
  messages: [
    {
      role: "system",
      content: "你是一個變數管理助手，請根據使用者需求設定變數"
    },
    {
      role: "user",
      content: "設定一個全域變數 userName 為 'Alice'"
    }
  ],
  response_format: openaiSchemas.variableOperationResult
});

// 3. 對話決策範例
const decisionResponse = await openai.chat.completions.create({
  model: "gpt-4o-2024-08-06",
  messages: [
    {
      role: "system",
      content: "你是一個對話流程決策助手，請根據當前對話狀況決定下一步行動"
    },
    {
      role: "user",
      content: "使用者說：'我想要查詢天氣'，目前在主選單流程"
    }
  ],
  response_format: openaiSchemas.conversationDecision
});

// 4. 表達式評估範例
const expressionResponse = await openai.chat.completions.create({
  model: "gpt-4o-2024-08-06",
  messages: [
    {
      role: "system",
      content: "你是一個表達式評估助手，請評估給定的表達式並返回結果"
    },
    {
      role: "user",
      content: "評估這個 JsonPath 表達式：$.Variables.userName，在變數上下文 {Variables: {userName: 'Bob'}} 中"
    }
  ],
  response_format: openaiSchemas.expressionEvaluation
});
*/
