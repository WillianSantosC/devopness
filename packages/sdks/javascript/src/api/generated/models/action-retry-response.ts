/* eslint-disable */
/**
 * devopness API
 * Devopness API - Painless essential DevOps to everyone 
 *
 * The version of the OpenAPI document: latest
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


import { ActionData } from './action-data';
import { ActionHookRequest } from './action-hook-request';
import { ActionResource } from './action-resource';
import { ActionStatus } from './action-status';
import { ActionStatusReasonCode } from './action-status-reason-code';
import { ActionSummary } from './action-summary';
import { ActionTarget } from './action-target';
import { ActionTriggeredFrom } from './action-triggered-from';
import { ActionType } from './action-type';
import { EnvironmentRelation } from './environment-relation';
import { ProjectRelation } from './project-relation';
import { RelatedAction } from './related-action';
import { UserRelation } from './user-relation';

/**
 * 
 * @export
 * @interface ActionRetryResponse
 */
export interface ActionRetryResponse {
    /**
     * The Id of the given action
     * @type {number}
     * @memberof ActionRetryResponse
     */
    id: number;
    /**
     * The ID of the pipeline executed by this action
     * @type {number}
     * @memberof ActionRetryResponse
     */
    pipeline_id: number | null;
    /**
     * The Id of the parent action that this action is a retry of
     * @type {number}
     * @memberof ActionRetryResponse
     */
    retry_of: number | null;
    /**
     * 
     * @type {ActionStatus}
     * @memberof ActionRetryResponse
     */
    status: ActionStatus;
    /**
     * Human readable version of action status
     * @type {string}
     * @memberof ActionRetryResponse
     */
    status_human_readable: string;
    /**
     * 
     * @type {ActionStatusReasonCode}
     * @memberof ActionRetryResponse
     */
    status_reason_code: ActionStatusReasonCode;
    /**
     * Human readable version of the status reason code
     * @type {string}
     * @memberof ActionRetryResponse
     */
    status_reason_human_readable: string;
    /**
     * 
     * @type {ActionType}
     * @memberof ActionRetryResponse
     */
    type: ActionType;
    /**
     * Human readable version of the action type
     * @type {string}
     * @memberof ActionRetryResponse
     */
    type_human_readable: string;
    /**
     * The permalink URL to the action details on Devopness web app
     * @type {string}
     * @memberof ActionRetryResponse
     */
    url_web_permalink: string;
    /**
     * 
     * @type {ActionData}
     * @memberof ActionRetryResponse
     */
    action_data: ActionData | null;
    /**
     * 
     * @type {ActionTriggeredFrom}
     * @memberof ActionRetryResponse
     */
    triggered_from: ActionTriggeredFrom;
    /**
     * 
     * @type {RelatedAction}
     * @memberof ActionRetryResponse
     */
    parent: RelatedAction | null;
    /**
     * List of related actions
     * @type {Array<RelatedAction>}
     * @memberof ActionRetryResponse
     */
    children: Array<RelatedAction>;
    /**
     * 
     * @type {UserRelation}
     * @memberof ActionRetryResponse
     */
    triggered_by_user?: UserRelation;
    /**
     * 
     * @type {ActionResource}
     * @memberof ActionRetryResponse
     */
    resource: ActionResource;
    /**
     * 
     * @type {ActionSummary}
     * @memberof ActionRetryResponse
     */
    summary: ActionSummary;
    /**
     * 
     * @type {EnvironmentRelation}
     * @memberof ActionRetryResponse
     */
    environment: EnvironmentRelation | null;
    /**
     * 
     * @type {ProjectRelation}
     * @memberof ActionRetryResponse
     */
    project: ProjectRelation | null;
    /**
     * List of actions dispatched to cloud resource targets
     * @type {Array<ActionTarget>}
     * @memberof ActionRetryResponse
     */
    targets?: Array<ActionTarget>;
    /**
     * 
     * @type {ActionHookRequest}
     * @memberof ActionRetryResponse
     */
    hook_requests?: ActionHookRequest;
    /**
     * The date and time when the action started execution (i.e., left the `pending/queued` status)
     * @type {string}
     * @memberof ActionRetryResponse
     */
    started_at: string | null;
    /**
     * The date and time when the action has finished execution
     * @type {string}
     * @memberof ActionRetryResponse
     */
    completed_at: string | null;
    /**
     * The date and time when the record was created
     * @type {string}
     * @memberof ActionRetryResponse
     */
    created_at: string;
    /**
     * The date and time when the record was last updated
     * @type {string}
     * @memberof ActionRetryResponse
     */
    updated_at: string;
}

