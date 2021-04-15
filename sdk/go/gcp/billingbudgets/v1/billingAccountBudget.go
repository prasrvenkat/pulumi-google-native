// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Creates a new budget. See [Quotas and limits](https://cloud.google.com/billing/quotas) for more information on the limits of the number of budgets you can create.
type BillingAccountBudget struct {
	pulumi.CustomResourceState

	// Required. Budgeted amount.
	Amount GoogleCloudBillingBudgetsV1BudgetAmountResponseOutput `pulumi:"amount"`
	// Optional. Filters that define which resources are used to compute the actual spend against the budget.
	BudgetFilter GoogleCloudBillingBudgetsV1FilterResponseOutput `pulumi:"budgetFilter"`
	// User data for display name in UI. The name must be less than or equal to 60 characters.
	DisplayName pulumi.StringOutput `pulumi:"displayName"`
	// Optional. Etag to validate that the object is unchanged for a read-modify-write operation. An empty etag will cause an update to overwrite other changes.
	Etag pulumi.StringOutput `pulumi:"etag"`
	// Resource name of the budget. The resource name implies the scope of a budget. Values are of the form `billingAccounts/{billingAccountId}/budgets/{budgetId}`.
	Name pulumi.StringOutput `pulumi:"name"`
	// Optional. Rules to apply to notifications sent based on budget spend and thresholds.
	NotificationsRule GoogleCloudBillingBudgetsV1NotificationsRuleResponseOutput `pulumi:"notificationsRule"`
	// Optional. Rules that trigger alerts (notifications of thresholds being crossed) when spend exceeds the specified percentages of the budget.
	ThresholdRules GoogleCloudBillingBudgetsV1ThresholdRuleResponseArrayOutput `pulumi:"thresholdRules"`
}

// NewBillingAccountBudget registers a new resource with the given unique name, arguments, and options.
func NewBillingAccountBudget(ctx *pulumi.Context,
	name string, args *BillingAccountBudgetArgs, opts ...pulumi.ResourceOption) (*BillingAccountBudget, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.BillingAccountsId == nil {
		return nil, errors.New("invalid value for required argument 'BillingAccountsId'")
	}
	if args.BudgetsId == nil {
		return nil, errors.New("invalid value for required argument 'BudgetsId'")
	}
	var resource BillingAccountBudget
	err := ctx.RegisterResource("gcp-native:billingbudgets/v1:BillingAccountBudget", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetBillingAccountBudget gets an existing BillingAccountBudget resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetBillingAccountBudget(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *BillingAccountBudgetState, opts ...pulumi.ResourceOption) (*BillingAccountBudget, error) {
	var resource BillingAccountBudget
	err := ctx.ReadResource("gcp-native:billingbudgets/v1:BillingAccountBudget", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering BillingAccountBudget resources.
type billingAccountBudgetState struct {
	// Required. Budgeted amount.
	Amount *GoogleCloudBillingBudgetsV1BudgetAmountResponse `pulumi:"amount"`
	// Optional. Filters that define which resources are used to compute the actual spend against the budget.
	BudgetFilter *GoogleCloudBillingBudgetsV1FilterResponse `pulumi:"budgetFilter"`
	// User data for display name in UI. The name must be less than or equal to 60 characters.
	DisplayName *string `pulumi:"displayName"`
	// Optional. Etag to validate that the object is unchanged for a read-modify-write operation. An empty etag will cause an update to overwrite other changes.
	Etag *string `pulumi:"etag"`
	// Resource name of the budget. The resource name implies the scope of a budget. Values are of the form `billingAccounts/{billingAccountId}/budgets/{budgetId}`.
	Name *string `pulumi:"name"`
	// Optional. Rules to apply to notifications sent based on budget spend and thresholds.
	NotificationsRule *GoogleCloudBillingBudgetsV1NotificationsRuleResponse `pulumi:"notificationsRule"`
	// Optional. Rules that trigger alerts (notifications of thresholds being crossed) when spend exceeds the specified percentages of the budget.
	ThresholdRules []GoogleCloudBillingBudgetsV1ThresholdRuleResponse `pulumi:"thresholdRules"`
}

type BillingAccountBudgetState struct {
	// Required. Budgeted amount.
	Amount GoogleCloudBillingBudgetsV1BudgetAmountResponsePtrInput
	// Optional. Filters that define which resources are used to compute the actual spend against the budget.
	BudgetFilter GoogleCloudBillingBudgetsV1FilterResponsePtrInput
	// User data for display name in UI. The name must be less than or equal to 60 characters.
	DisplayName pulumi.StringPtrInput
	// Optional. Etag to validate that the object is unchanged for a read-modify-write operation. An empty etag will cause an update to overwrite other changes.
	Etag pulumi.StringPtrInput
	// Resource name of the budget. The resource name implies the scope of a budget. Values are of the form `billingAccounts/{billingAccountId}/budgets/{budgetId}`.
	Name pulumi.StringPtrInput
	// Optional. Rules to apply to notifications sent based on budget spend and thresholds.
	NotificationsRule GoogleCloudBillingBudgetsV1NotificationsRuleResponsePtrInput
	// Optional. Rules that trigger alerts (notifications of thresholds being crossed) when spend exceeds the specified percentages of the budget.
	ThresholdRules GoogleCloudBillingBudgetsV1ThresholdRuleResponseArrayInput
}

func (BillingAccountBudgetState) ElementType() reflect.Type {
	return reflect.TypeOf((*billingAccountBudgetState)(nil)).Elem()
}

type billingAccountBudgetArgs struct {
	// Required. Budgeted amount.
	Amount            *GoogleCloudBillingBudgetsV1BudgetAmount `pulumi:"amount"`
	BillingAccountsId string                                   `pulumi:"billingAccountsId"`
	// Optional. Filters that define which resources are used to compute the actual spend against the budget.
	BudgetFilter *GoogleCloudBillingBudgetsV1Filter `pulumi:"budgetFilter"`
	BudgetsId    string                             `pulumi:"budgetsId"`
	// User data for display name in UI. The name must be less than or equal to 60 characters.
	DisplayName *string `pulumi:"displayName"`
	// Optional. Etag to validate that the object is unchanged for a read-modify-write operation. An empty etag will cause an update to overwrite other changes.
	Etag *string `pulumi:"etag"`
	// Optional. Rules to apply to notifications sent based on budget spend and thresholds.
	NotificationsRule *GoogleCloudBillingBudgetsV1NotificationsRule `pulumi:"notificationsRule"`
	// Optional. Rules that trigger alerts (notifications of thresholds being crossed) when spend exceeds the specified percentages of the budget.
	ThresholdRules []GoogleCloudBillingBudgetsV1ThresholdRule `pulumi:"thresholdRules"`
}

// The set of arguments for constructing a BillingAccountBudget resource.
type BillingAccountBudgetArgs struct {
	// Required. Budgeted amount.
	Amount            GoogleCloudBillingBudgetsV1BudgetAmountPtrInput
	BillingAccountsId pulumi.StringInput
	// Optional. Filters that define which resources are used to compute the actual spend against the budget.
	BudgetFilter GoogleCloudBillingBudgetsV1FilterPtrInput
	BudgetsId    pulumi.StringInput
	// User data for display name in UI. The name must be less than or equal to 60 characters.
	DisplayName pulumi.StringPtrInput
	// Optional. Etag to validate that the object is unchanged for a read-modify-write operation. An empty etag will cause an update to overwrite other changes.
	Etag pulumi.StringPtrInput
	// Optional. Rules to apply to notifications sent based on budget spend and thresholds.
	NotificationsRule GoogleCloudBillingBudgetsV1NotificationsRulePtrInput
	// Optional. Rules that trigger alerts (notifications of thresholds being crossed) when spend exceeds the specified percentages of the budget.
	ThresholdRules GoogleCloudBillingBudgetsV1ThresholdRuleArrayInput
}

func (BillingAccountBudgetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*billingAccountBudgetArgs)(nil)).Elem()
}

type BillingAccountBudgetInput interface {
	pulumi.Input

	ToBillingAccountBudgetOutput() BillingAccountBudgetOutput
	ToBillingAccountBudgetOutputWithContext(ctx context.Context) BillingAccountBudgetOutput
}

func (*BillingAccountBudget) ElementType() reflect.Type {
	return reflect.TypeOf((*BillingAccountBudget)(nil))
}

func (i *BillingAccountBudget) ToBillingAccountBudgetOutput() BillingAccountBudgetOutput {
	return i.ToBillingAccountBudgetOutputWithContext(context.Background())
}

func (i *BillingAccountBudget) ToBillingAccountBudgetOutputWithContext(ctx context.Context) BillingAccountBudgetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BillingAccountBudgetOutput)
}

type BillingAccountBudgetOutput struct {
	*pulumi.OutputState
}

func (BillingAccountBudgetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*BillingAccountBudget)(nil))
}

func (o BillingAccountBudgetOutput) ToBillingAccountBudgetOutput() BillingAccountBudgetOutput {
	return o
}

func (o BillingAccountBudgetOutput) ToBillingAccountBudgetOutputWithContext(ctx context.Context) BillingAccountBudgetOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(BillingAccountBudgetOutput{})
}